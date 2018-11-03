.PHONY: help init test run lint

TEST_PATH=./tests

.DEFAULT: help
help:
	@echo "make init"
	@echo "    Setup environment from Pipfile using pipenv"
	@echo "make test"
	@echo "    run tests"
	@echo "make run"
	@echo "    run project"

init:
	pipenv install

test:
	pipenv run python -m pytest --verbose --color=yes $(TEST_PATH)

run:
	pipenv run python pal/app.py

lint:
	pipenv run flake8 pal/*