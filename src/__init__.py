from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy

#application
app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "testcalendar131@gmail.com",
    "MAIL_PASSWORD": "xszfynrhtlagybbe"
}

app.config.update(mail_settings)

#SQLite database
db = SQLAlchemy(app) 

#routes
from src.routes import Home, Login, Register, Logout, Calendar

#models
from src.schemas import User