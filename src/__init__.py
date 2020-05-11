from flask import Flask
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy

#application
app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)

#SQLite database
db = SQLAlchemy(app) 

#routes
from src.routes import Home, Login, Register, Logout, Calendar, Settings

#models
from src.schemas import User

#init database
db.create_all()
