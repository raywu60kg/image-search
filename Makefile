help:  
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

ruff: ## ruff check
	ruff check src/ tests/ scripts/ && ruff format src/ tests/ scripts/

mypy: ## type check
	mypy --explicit-package-bases src tests scripts

server-dev: ## run dev server
	fastapi dev src/main.py

exec-db: ## exec db
	docker compose exec db psql -U image_search -d image_search

build-app-prod: ## docker build app prod
	docker build --target production -t image_search:prod -f ./docker/Dockerfile .
	
build-app-dev: ## docker build app dev
	docker build --target development -t image_search:dev -f ./docker/Dockerfile .

build-alembic-script: ## docker build alembic script
	docker build --target alembic -t image_search:alembic -f ./docker/Dockerfile .

