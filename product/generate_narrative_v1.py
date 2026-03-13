#!/usr/bin/env python3
"""
E-Solutions Live Narrative Generation v1

Generates AI narrative sections for a variance memo using the Anthropic API.

Usage:
    python generate_narrative_v1.py --input output/narrative_input.json --output output/narrative_output.json

    # With fallback to Opus:
    python generate_narrative_v1.py --input output/narrative_input.json --output output/narrative_output.json --fallback

    # Dry run (show rendered prompts without calling API):
    python generate_narrative_v1.py --input output/narrative_input.json --dry-run

See product/live_narrative_generation_spec_v1.md for full specification.
"""

import argparse
import datetime
import json
import os
import sys
import traceback
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional if ANTHROPIC_API_KEY is set in environment

import anthropic


# --- Configuration ---

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

SYSTEM_PROMPT_PATH = REPO_ROOT / "prompts" / "variance_memo_system_prompt_v1.md"
USER_PROMPT_TEMPLATE_PATH = REPO_ROOT / "prompts" / "variance_memo_user_prompt_v1.md"
OUTPUT_SCHEMA_PATH = REPO_ROOT / "product" / "narrative_output_schema_v1.json"

PRIMARY_MODEL = "claude-sonnet-4-6"
FALLBACK_MODEL = "claude-opus-4-6"
TEMPERATURE = 0.3
MAX_TOKENS = 4096
MAX_RETRIES = 1  # retry once on same model before fallback


# --- Prompt rendering ---

def load_system_prompt() -> str:
    """Load the system prompt markdown and extract the content."""
    text = SYSTEM_PROMPT_PATH.read_text()
    # Strip the markdown title line — send the content as-is
    return text


def render_user_prompt(narrative_input: dict) -> str:
    """Render the user prompt template with actual data from narrative input."""
    template = USER_PROMPT_TEMPLATE_PATH.read_text()

    company = narrative_input["company"]
    topline = narrative_input["topline"]
    meta = narrative_input["computation_metadata"]
    line_items = narrative_input["line_items"]

    # Filter to material items only
    material_items = [i for i in line_items if i.get("is_material", False)]

    # Build the rendered prompt
    rendered = template

    # Remove the template header (first 4 lines: title, blank, note, ---)
    lines = rendered.split("\n")
    start_idx = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i + 1
            break
    rendered = "\n".join(lines[start_idx:])

    # Replace placeholders
    rendered = rendered.replace("{{COMPANY_NAME}}", company["name"])
    rendered = rendered.replace("{{PERIOD_DISPLAY}}", company["period_display"])
    rendered = rendered.replace("{{PERIOD_CODE}}", company["period_code"])
    rendered = rendered.replace("{{COMPANY_STAGE}}", company.get("stage", "Unknown"))
    rendered = rendered.replace("{{ACCOUNTING_SYSTEM}}", company.get("accounting_system", "Unknown"))

    rendered = rendered.replace("{{TOPLINE_JSON}}", json.dumps(topline, indent=2))
    rendered = rendered.replace("{{MATERIAL_LINE_ITEMS_JSON}}", json.dumps(material_items, indent=2))

    rendered = rendered.replace("{{ROW_COUNT}}", str(meta["row_count"]))
    rendered = rendered.replace("{{MATERIAL_COUNT}}", str(meta["material_items"]))
    rendered = rendered.replace("{{THRESHOLD_DOLLARS}}", str(int(meta["materiality_threshold_dollars"])))
    rendered = rendered.replace("{{THRESHOLD_PERCENT}}", str(int(meta["materiality_threshold_percent"])))
    rendered = rendered.replace("{{HAS_PRIOR_PERIOD}}", str(meta["has_prior_period"]))

    # Handle conditional customer notes
    customer_notes = narrative_input.get("customer_notes")
    if customer_notes:
        rendered = rendered.replace("{{#IF CUSTOMER_NOTES}}", "")
        rendered = rendered.replace("{{/IF}}", "")
        rendered = rendered.replace("{{CUSTOMER_NOTES}}", customer_notes)
    else:
        # Remove the entire conditional block
        import re
        rendered = re.sub(
            r"\{\{#IF CUSTOMER_NOTES\}\}.*?\{\{/IF\}\}",
            "",
            rendered,
            flags=re.DOTALL,
        )

    return rendered.strip()


# --- Output validation ---

def validate_output(narrative: dict) -> list[str]:
    """Validate narrative output against required structure. Returns list of errors."""
    errors = []

    required_keys = [
        "executive_summary", "attention_items", "revenue_narratives",
        "expense_narratives", "risks", "recommended_actions",
    ]

    for key in required_keys:
        if key not in narrative:
            errors.append(f"Missing required key: {key}")

    if "executive_summary" in narrative:
        if not isinstance(narrative["executive_summary"], str) or len(narrative["executive_summary"]) < 20:
            errors.append("executive_summary must be a non-trivial string")

    if "attention_items" in narrative:
        items = narrative["attention_items"]
        if not isinstance(items, list) or len(items) < 1:
            errors.append("attention_items must be a non-empty list")

    if "revenue_narratives" in narrative:
        if not isinstance(narrative["revenue_narratives"], dict):
            errors.append("revenue_narratives must be an object")
        else:
            for code, narr in narrative["revenue_narratives"].items():
                if "drivers" not in narr:
                    errors.append(f"revenue_narratives[{code}] missing 'drivers'")

    if "expense_narratives" in narrative:
        if not isinstance(narrative["expense_narratives"], dict):
            errors.append("expense_narratives must be an object")
        else:
            for code, narr in narrative["expense_narratives"].items():
                if "drivers" not in narr:
                    errors.append(f"expense_narratives[{code}] missing 'drivers'")
                if "recurring" not in narr:
                    errors.append(f"expense_narratives[{code}] missing 'recurring'")
                elif narr["recurring"] not in ("Yes", "No", "Partially", "Timing", "TBD"):
                    errors.append(f"expense_narratives[{code}] invalid recurring value: {narr['recurring']}")

    if "risks" in narrative:
        if not isinstance(narrative["risks"], list) or len(narrative["risks"]) < 2:
            errors.append("risks must be a list with at least 2 items")
        else:
            for i, risk in enumerate(narrative["risks"]):
                for field in ("risk", "exposure", "trigger"):
                    if field not in risk:
                        errors.append(f"risks[{i}] missing '{field}'")

    if "recommended_actions" in narrative:
        if not isinstance(narrative["recommended_actions"], list) or len(narrative["recommended_actions"]) < 2:
            errors.append("recommended_actions must be a list with at least 2 items")
        else:
            for i, action in enumerate(narrative["recommended_actions"]):
                for field in ("action", "owner", "by_date"):
                    if field not in action:
                        errors.append(f"recommended_actions[{i}] missing '{field}'")

    return errors


# --- Artifact storage ---

def create_run_dir(base_dir: Path) -> Path:
    """Create a timestamped run directory for audit artifacts."""
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d_%H%M%S")
    run_dir = base_dir / f"run_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def save_artifact(run_dir: Path, filename: str, content: str | dict) -> Path:
    """Save an artifact to the run directory."""
    path = run_dir / filename
    if isinstance(content, dict):
        path.write_text(json.dumps(content, indent=2) + "\n")
    else:
        path.write_text(content + "\n" if not content.endswith("\n") else content)
    return path


# --- API call ---

def call_model(
    client: anthropic.Anthropic,
    model: str,
    system_prompt: str,
    user_prompt: str,
) -> tuple[str, dict]:
    """Call the Anthropic API and return (raw_text, usage_metadata)."""
    response = client.messages.create(
        model=model,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )

    raw_text = response.content[0].text

    usage = {
        "model": response.model,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "stop_reason": response.stop_reason,
    }

    return raw_text, usage


def parse_json_response(raw_text: str) -> dict:
    """Parse JSON from model response, handling common wrapping issues."""
    text = raw_text.strip()

    # Strip markdown code fences if present
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove first line (```json or ```) and last line (```)
        if lines[-1].strip() == "```":
            lines = lines[1:-1]
        else:
            lines = lines[1:]
        text = "\n".join(lines).strip()

    return json.loads(text)


# --- Main workflow ---

def generate(
    input_path: str,
    output_path: str,
    artifacts_dir: str = "output/artifacts",
    use_fallback: bool = False,
    dry_run: bool = False,
) -> dict:
    """Run the full narrative generation workflow."""

    # Load input
    narrative_input = json.loads(Path(input_path).read_text())
    print(f"Loaded narrative input: {input_path}")

    # Render prompts
    system_prompt = load_system_prompt()
    user_prompt = render_user_prompt(narrative_input)
    print(f"Rendered prompts (system: {len(system_prompt)} chars, user: {len(user_prompt)} chars)")

    # Create artifact directory
    run_dir = create_run_dir(Path(artifacts_dir))
    print(f"Artifact directory: {run_dir}")

    # Save input artifacts
    save_artifact(run_dir, "narrative_input.json", narrative_input)
    save_artifact(run_dir, "rendered_system_prompt.md", system_prompt)
    save_artifact(run_dir, "rendered_user_prompt.md", user_prompt)

    if dry_run:
        print("\n--- DRY RUN MODE ---")
        print(f"System prompt saved to: {run_dir}/rendered_system_prompt.md")
        print(f"User prompt saved to: {run_dir}/rendered_user_prompt.md")
        print("No API call made. Use rendered prompts in Claude chat for manual generation.")
        save_artifact(run_dir, "run_metadata.json", {
            "mode": "dry_run",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "input_path": input_path,
        })
        return {"status": "dry_run", "run_dir": str(run_dir)}

    # Initialize API client
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set. Set it in .env or environment.")
        save_artifact(run_dir, "error.txt", "ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Attempt generation
    models_to_try = [PRIMARY_MODEL]
    if use_fallback:
        models_to_try.append(FALLBACK_MODEL)

    last_error = None
    narrative = None
    raw_text = None
    usage = None
    model_used = None
    attempt = 0

    for model in models_to_try:
        for retry in range(MAX_RETRIES + 1):
            attempt += 1
            attempt_label = f"attempt {attempt} ({model}, try {retry + 1})"
            print(f"\nCalling API: {attempt_label}...")

            try:
                raw_text, usage = call_model(client, model, system_prompt, user_prompt)
                model_used = model

                # Save raw response
                save_artifact(run_dir, f"raw_response_attempt_{attempt}.txt", raw_text)
                save_artifact(run_dir, f"usage_attempt_{attempt}.json", usage)

                print(f"  Response received: {usage['output_tokens']} tokens, stop_reason={usage['stop_reason']}")

                # Parse JSON
                narrative = parse_json_response(raw_text)
                print(f"  JSON parsed successfully")

                # Validate structure
                validation_errors = validate_output(narrative)
                if validation_errors:
                    error_msg = f"Schema validation errors: {validation_errors}"
                    print(f"  WARNING: {error_msg}")
                    save_artifact(run_dir, f"validation_errors_attempt_{attempt}.json", {
                        "errors": validation_errors,
                        "attempt": attempt,
                    })
                    last_error = error_msg
                    narrative = None  # Force retry
                    continue

                print(f"  Schema validation: PASS")
                break  # Success

            except json.JSONDecodeError as e:
                last_error = f"JSON parse error: {e}"
                print(f"  ERROR: {last_error}")
                save_artifact(run_dir, f"error_attempt_{attempt}.txt", f"{last_error}\n\nRaw text:\n{raw_text}")
                narrative = None

            except anthropic.APIError as e:
                last_error = f"API error: {e}"
                print(f"  ERROR: {last_error}")
                save_artifact(run_dir, f"error_attempt_{attempt}.txt", str(e))
                narrative = None

            except Exception as e:
                last_error = f"Unexpected error: {e}"
                print(f"  ERROR: {last_error}")
                save_artifact(run_dir, f"error_attempt_{attempt}.txt", f"{last_error}\n\n{traceback.format_exc()}")
                narrative = None

        if narrative is not None:
            break  # Success, stop trying models

    # Save run metadata
    run_metadata = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "input_path": input_path,
        "output_path": output_path,
        "model_used": model_used,
        "total_attempts": attempt,
        "success": narrative is not None,
        "primary_model": PRIMARY_MODEL,
        "fallback_model": FALLBACK_MODEL if use_fallback else None,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
    }

    if usage:
        run_metadata["final_usage"] = usage

    if last_error and narrative is None:
        run_metadata["last_error"] = last_error

    save_artifact(run_dir, "run_metadata.json", run_metadata)

    # Handle failure
    if narrative is None:
        print(f"\nGENERATION FAILED after {attempt} attempts.")
        print(f"Last error: {last_error}")
        print(f"Artifacts saved to: {run_dir}")
        print("\nFallback options:")
        print("  1. Re-run with --fallback to try Claude Opus")
        print("  2. Copy rendered prompts from artifacts dir into Claude chat")
        print("  3. Write narrative sections manually using variance data")
        sys.exit(1)

    # Save validated output
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(narrative, indent=2) + "\n")
    save_artifact(run_dir, "validated_narrative_output.json", narrative)

    print(f"\nSUCCESS — Narrative generated and validated")
    print(f"  Model: {model_used}")
    print(f"  Attempts: {attempt}")
    print(f"  Output: {output_path}")
    print(f"  Artifacts: {run_dir}")

    # Print summary of what was generated
    rev_count = len(narrative.get("revenue_narratives", {}))
    exp_count = len(narrative.get("expense_narratives", {}))
    risk_count = len(narrative.get("risks", []))
    action_count = len(narrative.get("recommended_actions", []))
    print(f"  Revenue narratives: {rev_count}, Expense narratives: {exp_count}")
    print(f"  Risks: {risk_count}, Actions: {action_count}")

    return {
        "status": "success",
        "model": model_used,
        "attempts": attempt,
        "run_dir": str(run_dir),
        "output_path": output_path,
    }


def main():
    parser = argparse.ArgumentParser(
        description="E-Solutions Live Narrative Generation v1 — generate variance memo narratives using Claude API"
    )
    parser.add_argument(
        "--input", required=True,
        help="Path to narrative input JSON (from variance computation + company context)",
    )
    parser.add_argument(
        "--output", default="output/narrative_output.json",
        help="Path to write validated narrative output JSON (default: output/narrative_output.json)",
    )
    parser.add_argument(
        "--artifacts-dir", default="output/artifacts",
        help="Directory for generation audit artifacts (default: output/artifacts)",
    )
    parser.add_argument(
        "--fallback", action="store_true",
        help="Enable fallback to Claude Opus if Sonnet fails",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Render prompts and save to artifacts dir without calling the API",
    )
    args = parser.parse_args()

    generate(
        input_path=args.input,
        output_path=args.output,
        artifacts_dir=args.artifacts_dir,
        use_fallback=args.fallback,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
