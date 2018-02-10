PIP := env/bin/pip


env:
	python -m venv env

clean:
	rm -rf env

deps: env
	$(PIP) install -r requirements/base.txt


.PHONY: env clean deps
