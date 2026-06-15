.PHONY: test 

test:
	uv run pytest -v --cov

start-dev:
	uv run fastapi dev backend/app/main.py

docker-build-backed:
	docker compose up backend --build -d