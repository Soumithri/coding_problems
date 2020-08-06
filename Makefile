init:
	pip install pipenv
	pipenv install

test:
	pytest --cov-config=.coveragerc --cov=src

static-code-scan:
	sonar-scanner	