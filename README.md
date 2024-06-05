# RemoteLab API

[![Python](https://badgen.net/badge/language/python/orange?icon=python)]()
[![Flask](https://badgen.net/badge/framework/Flask/red?icon=)]()

_**Simple example of Flask API using microservices architecture, the application contained here develops some
functionalities for accessing the database and creating models and migrations.
Below are the steps required to run the database and the application backend
locally._

### Dependencies and Configuration

This project uses several libraries and tools to facilitate the development and execution of the application. The main dependencies and their functions are listed below:

1.  Flask: Web framework used to build the API.
2.  SQLAlchemy: ORM (Object-Relational Mapper) used to interact with the PostgreSQL database.
3.  marshmallow: simplified object serialization.
4.  python-dotenv: Library to manage environment variables.
5.  pymysql: Driver for MariaDB.
6.  PyJwt: library which allows you to encode and decode JSON Web Tokens.
11. unittest: Testing framework used for test-driven development (TDD).

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
