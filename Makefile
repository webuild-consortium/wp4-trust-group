# Makefile to run all CI tests locally
# Mirrors: .github/workflows/ci.yml, link-check.yml, mermaid-check.yml

.PHONY: all ci deps lint security link-check markdownlint mermaid test help

# Default: run all CI checks
all: ci

# Run everything that CI runs
ci: deps lint security link-check markdownlint mermaid
	@echo "All CI checks passed."

help:
	@echo "Targets:"
	@echo "  all, ci    - Run all CI checks (default)"
	@echo "  deps       - Install Python and Node dependencies"
	@echo "  lint       - flake8 (Python lint)"
	@echo "  security   - bandit + safety"
	@echo "  link-check - lychee link checker"
	@echo "  markdownlint - markdown lint"
	@echo "  mermaid    - validate Mermaid diagrams"
	@echo ""
	@echo "Requirements: Python 3.10+, Node 20+, lychee (cargo install lychee)"

# --- Dependencies ---
deps:
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt

# --- CI workflow (ci.yml) ---
lint:
	@echo "Running flake8..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

security:
	@echo "Running bandit..."
	@if [ -d src ]; then \
		bandit -r src/ -f json -o bandit-report.json; \
	else \
		echo "Skipping bandit: src/ not found"; \
	fi
	@echo "Running safety..."
	safety check --output screen

# --- Link check workflow (link-check.yml) ---
# Lychee uses lychee.toml for exclude patterns (single source of truth)
link-check:
	@echo "Running lychee link check..."
	@command -v lychee >/dev/null 2>&1 || { echo "Install lychee: cargo install lychee"; exit 1; }
	lychee .

# Markdownlint uses .markdownlint-cli2.jsonc for globs (single source of truth)
markdownlint:
	@echo "Running markdownlint..."
	npx --yes markdownlint-cli2

# --- Mermaid check workflow (mermaid-check.yml) ---
mermaid:
	@echo "Validating Mermaid diagrams..."
	@files=$$(grep -rl '```mermaid' --include='*.md' . 2>/dev/null || true); \
	if [ -z "$$files" ]; then \
		echo "No markdown files with Mermaid diagrams found."; \
	else \
		failed=0; \
		for f in $$files; do \
			echo "Validating: $$f"; \
			out=$$(mktemp -u /tmp/mermaid-XXXXX.svg); \
			if ! npx mmdc -p .github/puppeteer-config.json -i "$$f" -o "$$out" -b transparent 2>/dev/null; then \
				echo "::error::Mermaid render failed in $$f"; \
				failed=1; \
			fi; \
			rm -f "$$out" "$${out%.svg}"-*.svg 2>/dev/null || true; \
		done; \
		exit $$failed; \
	fi

# Optional: pytest (commented out in CI but available)
test:
	@echo "Running pytest..."
	@if [ -d tests ]; then \
		pytest tests/ --cov=src --cov-report=xml --cov-report=html 2>/dev/null || pytest tests/; \
	else \
		echo "No tests/ directory found."; \
	fi
