# Fitness Tracker API

[![Circle CI Badge](https://circleci.com/gh/Belax8/ft-api/tree/master.svg?style=shield&circle-token=bee489f88316bda9fd0a6a32d02ed5bb977999e4)](https://circleci.com)

This project was built to show how to use [Django Rest Framework Signature](https://github.com/Skylude/django-rest-framework-signature) and [Django Rest Framework Simplify](https://github.com/Skylude/django-rest-framework-simplify).

## Setup

### Setup Postgres
```
create user ft with password 'test1234' CREATEDB;
create database fitness_tracker_local with owner ft;
```

### Setup Python Environment
```
virtualenv ~/env/ft-api-env --python=python3
vi ~/.bashrc
alias ftapi='source ~/env/ft-api-env/bin/activate; cd ~/ft-api'
source ~/.bashrc
ftapi
pip install -r requirements.txt
```

#### If you get an `egg_info` error
```
sudo apt-get install libmysqlclient-dev
```


## Server
```
python manage.py runserver
```


## Tests
```
python manage.py test
```
