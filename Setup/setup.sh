#!/bin/bash

# cd home
cd ~
# install dependencies
if [ $"command -v pip3 | wc -l" > 0 ]
then
    pip3 install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn
else 
    pip install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn
fi
