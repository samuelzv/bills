.PHONY: test start-dev

test:
	uv run pytest -v --cov

start-dev:
	uv run fastapi dev backend/app/main.py
