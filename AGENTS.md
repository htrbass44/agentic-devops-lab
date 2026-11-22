# AGENTS.md

## Setup
pip install -r requirements-dev.txt

## Test
pytest -q

## Lint
ruff check .

## Rules
- Do not modify files under .github/workflows/ unless the issue explicitly asks for it.
- Keep changes minimal and focused on the issue.
