#!/bin/bash

# cd home
cd ~
# install dependencies
if [ $"command -v pip3 | wc -l" > 0 ]
then
    pip3 install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx flask-mail
else 
    pip install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx flask-mail
fi
