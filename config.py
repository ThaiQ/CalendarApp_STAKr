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
    SQLALCHEMY_DATABASE_URI = 'postgres://gmlzcvvnmvwhio:d8514894e41e282962315454ba44cc90a8f545397e22b098aa7aedb5be09efad@ec2-52-70-15-120.compute-1.amazonaws.com:5432/d5u64p2nhl64c1'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
