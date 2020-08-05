# coding_problems

[![Build Status](https://travis-ci.org/Soumithri/coding_problems.svg?branch=master)](https://travis-ci.org/Soumithri/coding_problems)
[![codecov](https://codecov.io/gh/Soumithri/coding_problems/branch/master/graph/badge.svg)](https://codecov.io/gh/Soumithri/coding_problems)

Coding problems is a repository which has solutions to top interview coding questions in Python 3.

## Requirements

[Docker desktop for MAC/PC/Linux](https://docs.docker.com/get-docker/)

## Usage

Python scripts are best run through ``dockers`` since it promotes uniformness across different operating systems.

```bash
docker-compose run --rm code python src/arrays/hello_world.py
```

To run all unit tests:
```bash
docker-compose run --rm code pytest 
```

To run a specific unit test:
```bash
docker-compose run --rm code pytest src/arrays/tests/test_hello_world.py
```

## Code Coverage
To find the code coverage, run the below commands:

1. If the container ``app``is already present, run:
```bash
docker container exec -it app pytest --cov-config=.coveragerc --cov=src
```
2. If there is no running container, run:
```bash
docker-compose run --rm code pytest --cov-config=.coveragerc --cov=src
```

Note: By default, unit tests coverage is disabled. 
To enable test coverage, change the ``omit`` section in ``.coveragerc`` file to:
```bash
omit = *__init__*
```
More information on ``.coveragerc`` can be found in this [link](https://coverage.readthedocs.io/en/coverage-5.0.4/config.html)
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
