#!/usr/bin/env bash
# E-Solutions PDF Generation v1
# Converts markdown deliverables to styled PDFs using WeasyPrint.
#
# Usage:
#   ./ops/generate_pdfs_v1.sh memo       # Generate memo PDF only
#   ./ops/generate_pdfs_v1.sh pilot      # Generate pilot package PDF only
#   ./ops/generate_pdfs_v1.sh all        # Generate all PDFs
#
# Requirements:
#   - Python venv at .venv/ with weasyprint and markdown installed
#   - pip install weasyprint markdown (included in requirements.txt)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON="$REPO_ROOT/.venv/bin/python"

# Check dependencies
if [ ! -f "$PYTHON" ]; then
    echo "ERROR: Python venv not found at .venv/. Run: make setup"
    exit 1
fi

$PYTHON -c "import weasyprint; import markdown" 2>/dev/null || {
    echo "ERROR: Required packages missing. Run: .venv/bin/pip install weasyprint markdown"
    exit 1
}

generate_pdf() {
    local md_file="$1"
    local css_file="$2"
    local pdf_file="$3"
    local label="$4"

    if [ ! -f "$md_file" ]; then
        echo "ERROR: Source file not found: $md_file"
        return 1
    fi

    echo "Generating $label..."
    echo "  Source: $md_file"
    echo "  Style:  $css_file"
    echo "  Output: $pdf_file"

    $PYTHON -c "
import markdown
import weasyprint
import sys

md_path = '$md_file'
css_path = '$css_file'
pdf_path = '$pdf_file'

# Read markdown
with open(md_path, 'r') as f:
    md_text = f.read()

# Convert to HTML with table support
html_body = markdown.markdown(md_text, extensions=['tables', 'sane_lists'])

# Wrap in full HTML document
html = f'''<!DOCTYPE html>
<html>
<head><meta charset=\"utf-8\"></head>
<body>
{html_body}
</body>
</html>'''

# Read CSS
with open(css_path, 'r') as f:
    css_text = f.read()

# Generate PDF
doc = weasyprint.HTML(string=html)
css = weasyprint.CSS(string=css_text)
doc.write_pdf(pdf_path, stylesheets=[css])

print(f'  Done: {pdf_path}')
"
}

case "${1:-all}" in
    memo)
        generate_pdf \
            "$REPO_ROOT/deliverables/generated_memo_draft_v2.md" \
            "$REPO_ROOT/ops/memo_style.css" \
            "$REPO_ROOT/deliverables/generated_memo_draft_v2.pdf" \
            "Variance Memo PDF"
        ;;
    pilot)
        generate_pdf \
            "$REPO_ROOT/gtm/pilot_package_v2.md" \
            "$REPO_ROOT/ops/pilot_style.css" \
            "$REPO_ROOT/gtm/pilot_package_v2.pdf" \
            "Pilot Package PDF"
        ;;
    sample)
        generate_pdf \
            "$REPO_ROOT/deliverables/sample_variance_memo_v2.md" \
            "$REPO_ROOT/ops/memo_style.css" \
            "$REPO_ROOT/deliverables/sample_variance_memo_v2.pdf" \
            "Sample Variance Memo PDF"
        ;;
    all)
        generate_pdf \
            "$REPO_ROOT/deliverables/generated_memo_draft_v2.md" \
            "$REPO_ROOT/ops/memo_style.css" \
            "$REPO_ROOT/deliverables/generated_memo_draft_v2.pdf" \
            "Variance Memo PDF"
        echo ""
        generate_pdf \
            "$REPO_ROOT/gtm/pilot_package_v2.md" \
            "$REPO_ROOT/ops/pilot_style.css" \
            "$REPO_ROOT/gtm/pilot_package_v2.pdf" \
            "Pilot Package PDF"
        echo ""
        generate_pdf \
            "$REPO_ROOT/deliverables/sample_variance_memo_v2.md" \
            "$REPO_ROOT/ops/memo_style.css" \
            "$REPO_ROOT/deliverables/sample_variance_memo_v2.pdf" \
            "Sample Variance Memo PDF"
        ;;
    *)
        echo "Usage: $0 {memo|pilot|sample|all}"
        exit 1
        ;;
esac

echo ""
echo "=== PDF generation complete ==="
