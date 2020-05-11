import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'new-secret-key-for-cross-site-attack'

    #store data at the current directory folder
    SQLALCHEMY_DATABASE_URI = 'postgres://ynemtuwbjnolil:6d55ec6c15595cf68d4ba4ed838e48e0d908d3ff81e2b2ff95a0b1549d26f731@ec2-52-200-119-0.compute-1.amazonaws.com:5432/d6ot3si03noign'
    SQLALCHEMY_TRACK_MODIFICATIONS = False