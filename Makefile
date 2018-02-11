ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip
PYTHON := $(ENV)/bin/python
MANAGE := $(PYTHON) manage.py


start:
	$(MANAGE) runserver

test:
	$(ENV)/bin/coverage run manage.py test
	$(ENV)/bin/coverage report
	$(ENV)/bin/flake8

env:
	$(shell which python) -m venv $(ENV)

clean:
	rm -rf env

deps: env
	$(PIP) install -r requirements/base.txt

dev-deps: deps
	$(PIP) install -r requirements/dev.txt

new-db: deps
	dropdb dmf --if-exists
	createdb dmf
	$(MANAGE) makemigrations
	$(MANAGE) migrate


.PHONY: env clean deps dev-deps new-db start test
