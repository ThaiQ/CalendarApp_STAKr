@ECHO off

REM cd home
cd ~
REM install dependencies
WHERE pip3
if %ERRORLEVEL% NEQ 1 (
    call pip3 install flask flask-wtf flask-sqlalchemy flask-login
) else (
    call pip install flask flask-wtf flask-sqlalchemy flask-login
)