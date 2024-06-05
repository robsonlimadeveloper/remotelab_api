# RemoteLab API

[![Python](https://badgen.net/badge/language/python/orange?icon=python)]()
[![Flask](https://badgen.net/badge/framework/Flask/red?icon=)]()

_**Simple example of Flask API using microservices architecture, the application contained here develops some
functionalities for accessing the database and creating models and migrations.
Below are the steps required to run the database and the application backend
locally._

### Prerequisites

*_**[Docker and Docker-Compose](https://www.docker.com/products/docker-desktop/)**_ installed on the environment.*

### Installation
1. Build project

```sh
$ docker-compose up --build -d
```

2. First migration

```sh
$ docker exec -it remotelab_dev_app bash
@container $ rm -rf migrations

@container $ flask db init

@container $ flask db migrate

@container $ flask db upgrade

@container $ flask seed
```

## Container database


```sh
$ docker exec -it remotelab_dev_db bash
@container $ mysql -u root -p

@container $ >password root
```

## Swagger
```
http://localhost:4010/remotelab-api/swagger/
```

## Run tests (unittest)

```sh
$ docker exec -it remotelab_dev_app bash

@container $ python -m unittest discover -v

```
