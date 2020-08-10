import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'new-secret-key-for-cross-site-attack'

    '''
        Pick one database location from below
        1. on local machine
        2. on Heroku's Postgres server
    '''
    #store data at the current directory folder (local machine)
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    #store data at Heroku's Postgres adds-on (in Heroku's settings)
    SQLALCHEMY_DATABASE_URI = 'postgres://hflqpmkxpzcbvj:af66596df83f5659fd3ba61f5ac29d34471e7c189259696f294913519caf695f@ec2-34-194-198-176.compute-1.amazonaws.com:5432/dc3i70uvlpldhu'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
