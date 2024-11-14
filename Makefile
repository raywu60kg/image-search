help:  
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

ruff: ## ruff check
	ruff check src/ tests/ scripts/ && ruff format src/ tests/ scripts/

mypy: ## type check
	mypy --explicit-package-bases src tests scripts

server-dev: ## run dev server
	fastapi dev src/main.py