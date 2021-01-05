# REMOTELAB (API)

## Proposição de Layout

Baseada no Framework Flask, a aplicação aqui contida desenvolve algumas
funcionalidades para acesso ao banco de dados e criação de modelos e migrações

## Install Docker

```sh
curl -sSL https://get.docker.com | sh
```
## No Raspberry

2. Add permission to Pi User to run Docker Commands
```sh
sudo usermod -aG docker pi && sudo reboot

```

## Instalação de dependências
```sh
sudo apt-get install -y libffi-dev libssl-dev python3 python3-pip && sudo apt-get remove python-configparser
```
## Install Docker Compose

```sh
sudo pip3 -v install docker-compose
```

## Iniciando o ambiente de desenvolvimento

1. levantando o container

```sh
$ docker-compose up --build -d
```

Opcional: levantando container debug

```sh
$ docker-compose up
```

2. Acesso ao container e criação do banco de dados

```sh
$ docker exec -it remotelab_dev_db bash
@container $ /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P '$@pqfe#777' -Q 'CREATE DATABASE remotelab;'
```

Opcional: Para remover remover o banco e o seus dados

```sh
$ docker rm remotelab_dev_db
$ docker volume rm docker-flask_db_data
```

3. Primeira migration

```sh
$ docker exec -it remotelab_dev_app bash
@container $ rm -rf migrations

@container $ flask db init

@container $ flask db migrate

@container $ flask db upgrade

@container $ flask seed
```