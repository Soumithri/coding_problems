init:
	export PYTHONPATH=$PYTHONPATH:$(pwd)
    pip install pipenv
    pipenv install

test:
    pytest --cov-config=.coveragerc --cov=src