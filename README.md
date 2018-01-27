# Fitness Tracker API


## Setup

### Setup Posgres
```
create user ft with password 'test1234' CREATEDB;
create database fitness_tracker_local with owner ft;
```

### Setup Python
```
pip install -r requirements.txt
```


## Server
```
python manage.py runserver
```


## Tests
```
python manage.py test
```
