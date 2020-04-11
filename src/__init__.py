from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

#application
app = Flask(__name__)
app.config.from_object(Config)

#SQLite database
db = SQLAlchemy(app) 

#routes
from src.routes import Home, Login

#models
from src.schemas import Post, User