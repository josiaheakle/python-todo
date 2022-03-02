from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# App init
app = Flask(__name__) # app instance
app.config.from_object(Config) # set env variables

# DB init
db = SQLAlchemy(app) # db connection object
migrate = Migrate(app, db) # db migration object

# Login Managaer
login = LoginManager(app)

from app import routes, models # allow for routes and models to imported properties of app
