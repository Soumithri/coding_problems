# coding_problems

[![Build Status](https://travis-ci.org/Soumithri/coding_problems.svg?branch=master)](https://travis-ci.org/Soumithri/coding_problems)

Coding problems is a repository which has solutions to top interview coding questions in Python 3.

## Requirements

[Docker desktop for MAC/PC/Linux](https://docs.docker.com/get-docker/)

## Usage

Python scripts are best run through ``dockers`` since it promotes uniformness across different operating systems.

First, build the docker file:
```bash
docker-compose build
```

Run the python script.
```bash
docker-compose run --rm code python src/arrays/hello_world.py
```
Note: ``code`` parameter in the above command refers to the name of the service in docker-compose.yml

To run all unit tests:
```bash
docker-compose run --rm code pytest 
```

To run a specific unit test:
```
docker-compose run --rm code pytest src/arrays/tests/test_hello_world.py
```
Note: 
By default, we will be running python scripts on the fly. However if you want to have container
always up and running, run the bellow docker command.

```bash
docker-compose build
docker-compose run -d -p 80:80 --name app code
```

Now run the python scripts and unit tests in the running container
```bash
docker container exec -it app python src/arrays/hello_world.py
docker container exec -it app pytest
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
