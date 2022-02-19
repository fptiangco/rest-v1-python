[![codecov](https://codecov.io/gh/fptiangco/rest-v1-python/branch/main/graph/badge.svg?token=3BXDA33460)](https://codecov.io/gh/fptiangco/rest-v1-python) [![Push](https://github.com/fptiangco/rest-v1-python/actions/workflows/trigger_push.yaml/badge.svg)](https://github.com/fptiangco/rest-v1-python/actions/workflows/trigger_push.yaml) [![Docker](https://img.shields.io/docker/cloud/build/fptiangco/rest-v1-python?label=Docker&style=flat)](https://hub.docker.com/r/fptiangco/rest-v1-python/builds)

Quickstart

Local/Virtualenv:
```
# Install
pip install -r src/requirements.txt
# Test and Coverage
pytest --cov
# Run
export FLASK_APP=src/server.py; flask run -h 0.0.0.0 -p 8080
```
Docker
```
# Build
docker build . -t rest-v1-python
# Test
docker run rest-v1-python pytest --cov
# Run
docker run -p 5000:5000 rest-v1-python
```