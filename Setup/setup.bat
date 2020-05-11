@ECHO off

REM cd home
cd ~
REM install dependencies
WHERE pip3
if %ERRORLEVEL% NEQ 1 (
    call pip3 install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2 pipenv
    call pipenv install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2 pipenv
) else (
    call pip install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2 pipenv
    call pipenv install flask flask-wtf flask-sqlalchemy flask-login pytest sphinx wtforms_components email_validator gunicorn psycopg2 pipenv
)