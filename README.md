# coding_problems

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
```
docker-compose run --rm code pytest src/arrays/tests/test_hello_world.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
