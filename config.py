import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'new-secret-key-for-cross-site-attack'

    #store data at the current directory folder
    SQLALCHEMY_DATABASE_URI = 'postgres://dgxathrfwxaiet:9fb8f174a782b6ce57b450b980a17dc39acac79bda132fb40cbdfe660fe4b2b0@ec2-52-207-25-133.compute-1.amazonaws.com:5432/dd5egk237qbuus'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
