init:
	pip install pipenv
	pipenv install

test:
	pytest --cov-config=.coveragerc --cov=src

static_code_scan:
	sonar-scanner