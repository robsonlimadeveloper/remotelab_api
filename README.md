## REMOTELAB (API)

# Proposição de Layout

Baseada no Framework Flask, a aplicação aqui contida desenvolve algumas
funcionalidades para acesso ao banco de dados e criação de modelos e migrações.
Abaixo os passos necessários para executar o banco de dados e o backend da aplicação
localmente.

# 1 - Instalação do Docker && Docker Compose no Raspberry Pi

```sh
curl -sSL https://get.docker.com | sh
```

## Add permission to Pi User to run Docker Commands

```sh
sudo usermod -aG docker pi && sudo reboot

```

## Instalação de dependências

```sh
sudo apt-get install -y libffi-dev libssl-dev python3 python3-pip git && sudo apt-get remove python-configparser
```
## Install Docker Compose

```sh
sudo pip3 -v install docker-compose
```

# 2 - Clone o respositório

```sh
sudo git clone https://github.com/robsonlimadeveloper/remotelab_api.git
```

## Entre na pasta

```sh
cd remotelab_api
```

# 3 - Iniciando o ambiente de desenvolvimento

1. levantando o container

```sh
$ docker-compose up --build -d
```

2. Primeira migration

```sh
$ docker exec -it remotelab_dev_app bash
@container $ rm -rf migrations

@container $ flask db init

@container $ flask db migrate

@container $ flask db upgrade

@container $ flask seed
```

# Extras

## Acesso ao container do banco de dados

No Docker raspberry

```sh
$ docker exec -it remotelab_dev_db bash
@container $ mysql -u root -p

@container $ >password root
```

No Docker PC

```sh
$ docker exec -it remotelab_dev_db bash
@container $ mysql -u root -p

@container $ >password root
```

## levantando container em modo debug

```sh
$ docker-compose up
```

## Para remover remover o banco e o seus dados

No Docker raspberry

```sh
$ docker-compose down
$ docker volume rm docker-flask_db_data
```

## [Temporário] ENDPOINTS

No arquivo endpoints.md há a lista de endpoints disponíveis até o momento.
Esse arquivo será usando temporáriamente enquanto o Swagger Doc é implementado no sistema.