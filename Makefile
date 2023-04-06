all:
	python3 templater.py

test:
	pipenv run pytest

lazy: all
	git commit -am "Lazy auto commit"
	git push origin master

preview:
	python3 -m http.server

.PHONY: all test

