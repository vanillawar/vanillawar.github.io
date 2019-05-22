all:
	pipenv run python3 templater.py

test:
	pipenv run pytest

preview:
	python3 -m http.server

.PHONY: all test

