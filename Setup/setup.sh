#!/bin/bash

# cd home
cd ~
# install dependencies
if [ $"command -v pip3 | wc -l" > 0 ]
then
    pip3 install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2-binary pipenv
    pipenv install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2-binary pipenv
else 
    pip install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2-binary pipenv
    pipenv install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2-binary pipenv
fi
