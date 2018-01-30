# Fitness Tracker API


## Setup

### Setup Postgres
```
create user ft with password 'test1234' CREATEDB;
create database fitness_tracker_local with owner ft;
```

### Setup Python
```
virtualenv ~/env/ft-api-env --python=python3
vi ~/.bashrc
alias ftapi='source ~/env/ft-api-env/bin/activate; cd ~/ft-api'
source ~/.bashrc
ftapi
pip install -r requirements.txt
```

#### If egg_info error
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
