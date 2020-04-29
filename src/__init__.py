from flask import Flask
from flask_login import LoginManager
from config import Config, mail_settings
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedSerializer
from flask_mail import Mail

#application config
app = Flask(__name__)
app.config.from_object(Config)
app.config.update(mail_settings)

#login manager
login = LoginManager(app)

#SQLite database
db = SQLAlchemy(app) 

#mailing
mail = Mail(app)
serializer = TimedSerializer('serializer-secret')
salt = 'secrete-key-for-email-token'

#routes
from src.routes import Home, Login, Register, Logout, Calendar

#models
from src.schemas import User
