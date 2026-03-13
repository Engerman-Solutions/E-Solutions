# E-Solutions Pilot Pipeline
# Usage: make validate FILE=data/gl.csv PERIOD=2026-02
#        make compute FILE=data/gl.csv
#        make assemble
#        make sample-pipeline  (runs full pipeline on sample data)

PYTHON = .venv/bin/python
OUTPUT_DIR = output
SAMPLE_DATA = deliverables/sample_variance_data_v1.csv
SAMPLE_CONTEXT = product/sample_company_context_v1.json
SAMPLE_NARRATIVE = product/sample_narrative_output_v1.json

.PHONY: setup validate compute assemble sample-pipeline clean

setup:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

validate:
	$(PYTHON) product/validation_checks_v1.py $(FILE) $(if $(PERIOD),--period $(PERIOD)) $(if $(OUT),--output $(OUT))

compute:
	@mkdir -p $(OUTPUT_DIR)
	$(PYTHON) product/variance_computation_v1.py $(FILE) --pretty --output $(OUTPUT_DIR)/variance_output.json

assemble:
	$(PYTHON) product/assemble_memo_v1.py \
		--variance $(OUTPUT_DIR)/variance_output.json \
		--narrative $(NARRATIVE) \
		--context $(CONTEXT) \
		--output $(OUTPUT)

sample-pipeline:
	@echo "=== E-Solutions Sample Pipeline ==="
	@mkdir -p $(OUTPUT_DIR)
	@echo "Step 1: Validate..."
	$(PYTHON) product/validation_checks_v1.py $(SAMPLE_DATA) --period 2026-02 --output $(OUTPUT_DIR)/validation_report.json
	@echo ""
	@echo "Step 2: Compute variances..."
	$(PYTHON) product/variance_computation_v1.py $(SAMPLE_DATA) --pretty --output $(OUTPUT_DIR)/variance_output.json
	@echo ""
	@echo "Step 3: Assemble memo..."
	$(PYTHON) product/assemble_memo_v1.py \
		--variance $(OUTPUT_DIR)/variance_output.json \
		--narrative $(SAMPLE_NARRATIVE) \
		--context $(SAMPLE_CONTEXT) \
		--output deliverables/generated_memo_draft_v1.md
	@echo ""
	@echo "=== Pipeline complete ==="
	@echo "Output: deliverables/generated_memo_draft_v1.md"

clean:
	rm -rf $(OUTPUT_DIR)
