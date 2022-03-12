* Tests [![codecov](https://codecov.io/gh/fptiangco/rest-v1-python/branch/main/graph/badge.svg?token=3BXDA33460)](https://codecov.io/gh/fptiangco/rest-v1-python) [![Push](https://github.com/fptiangco/rest-v1-python/actions/workflows/trigger_push.yaml/badge.svg)](https://github.com/fptiangco/rest-v1-python/actions/workflows/trigger_push.yaml) 
* Docker [![Docker](https://img.shields.io/docker/cloud/build/fptiangco/rest-v1-python?label=Docker&style=flat)](https://hub.docker.com/r/fptiangco/rest-v1-python/builds) ![Docker Pulls](https://img.shields.io/docker/pulls/fptiangco/rest-v1-python)
* QA [![Updates](https://pyup.io/repos/github/fptiangco/rest-v1-python/shield.svg)](https://pyup.io/repos/github/fptiangco/rest-v1-python/)

### Quickstart
* A utility service that returns 'v1'

##### Local flask run
```
# Install
pip install -r src/requirements.txt

# Python package scan
safety check
# Test and coverage
pytest --cov

# Run on localhost:5000
export FLASK_APP=src/server.py; flask run -h 0.0.0.0 -p 5000
```
##### Docker build + run
```
# Build
docker build . -t rest-v1-python

# Image scan
docker scan rest-v1-python
# Python package scan
docker run rest-v1-python safety check
# Test and coverage
docker run rest-v1-python pytest --cov

# Run on localhost:5000
docker run -p 5000:5000 rest-v1-python
```
##### Dockerhub run
```
docker run -p 5000:5000 fptiangco/rest-v1-python
```
##### View
http://localhost:5000
