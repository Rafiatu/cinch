# Cinch API

![Cinch API](https://github.com/Rafiatu/cinch/workflows/Cinch%20API/badge.svg?branch=main)

API Service backing client interfaces

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description

Cinch API service is a standalone service that web and mobile interfaces will depend on. The API service will also be interacting with different services for storage, notification, retrieving and receiving data for other services that depends on it, such services include but not limited to Database Service, Payment Service, File Storage Service etc.

## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/Rafiatu/cinch.git` to clone the project repository.

Change directory into the project folder `cd cinch` and build the base python image used for the project that was specified in ***dockerfile*** by running ` docker build . ` *Note the dot (.) at end of the command*.

Spin up other services needed for the project that are specified in ***docker-compose.yml*** file by running the command `docker-compose up`. At this moment, your project should be up and running with a warning that *you have unapplied migrations*.

Open up another terminal and run this command `docker-compose exec api python project/manage.py makemigrations` for creating new migrations based on the models defined and also run `docker compose exec api python project/manage.py migrate` to apply migrations.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/Rafiatu/cinch.git
2. cd cinch
3. docker build .
4. docker-compose up
5. docker-compose exec api python project/manage.py makemigrations
6. docker-compose exec api python project/manage.py migrate
```

## Running Tests

Currently, truthy tests has been provided in each of the application defined in the project, before running the tests with the following command make sure that your api service is up and running.

```docker
docker-compose exec api python project/manage.py test
docker-compose exec api flake8
```

## License

The MIT License - Copyright (c) 2020 - Rafihatu Bello and Co.

