import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'new-secret-key-for-cross-site-attack'

    #store data at the current directory folder
    SQLALCHEMY_DATABASE_URI = 'postgres://ptdzzknfatdeot:56751518d0a222e3e56f60fb62ba9274afb71f8c8e8817a1a62c86c3e75dd423@ec2-50-17-90-177.compute-1.amazonaws.com:5432/dantgds9r370'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
