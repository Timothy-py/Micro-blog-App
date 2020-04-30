from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


appInstance = Flask(__name__)
appInstance.config.from_object(Config)
db = SQLAlchemy(app=appInstance)
migrate = Migrate(app=appInstance, db=db)

from app import routes, models