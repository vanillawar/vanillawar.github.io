all:
	pipenv run python3 templater.py

test:
	pipenv run pytest

.PHONY: all test

