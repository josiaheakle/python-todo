from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__) # app instance
app.config.from_object(Config) # set env variables

db = SQLAlchemy(app) # db connection object
migrate = Migrate(app, db) # db migration object

from app import routes, models
