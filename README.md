<h1 align="center">
  <br>
   RemoteLab API - Example
  <br>
</h1>

<p align="center">  
<img src="https://badgen.net/badge/language/python/yellow?icon=python">
<img src="https://badgen.net/badge/framework/flask/pink?icon=">
<img src="https://badgen.net/badge/orm/sqlalchemy/red?icon=">
<img src="https://badgen.net/badge/database/mysql/blue?icon=">
<img src="https://badgen.net/badge/tests/unittest/blue?icon=">
</p>
<p align="center">
<a href='https://ko-fi.com/V7V717GRV1' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
</p>

<p align="justify">
RemoteLab API is a simple RESTful API example built with Python using the Flask framework, SQLAlchemy as the ORM, and MariaDB as the database. The project is containerized with Docker and orchestrated with Docker Compose for easy deployment and development.

</p>

<p><strong>Develop with:</strong></p>

<p align="left">
	
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,flask,mysql,git,docker,vscode" />
  </a>
</p>

## Features
<p align="left">
  
- <strong>CRUD Operations:</strong> Create, read, update, and delete database records.

- <strong>JWT Authentication:</strong> Secure authentication using JSON Web Tokens.

- <strong>Data Validation:</strong> Ensures data integrity through model-defined validations.

- <strong>API Documentation:</strong> Interactive API documentation provided with Swagger UI.
</p>

## Technologies Used

<p align="left">
<strong>Language:</strong> Python 3.8+

<strong>Web Framework:</strong> Flask 1.1.2

<strong>ORM:</strong> SQLAlchemy

<strong>Database:</strong> MariaDB

<strong>Containerization:</strong> Docker & Docker Compose
</p>

## Getting Started:

Follow the steps below to set up and run the database and backend application locally.

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
