from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_login import LoginManager


appInstance = Flask(__name__)
appInstance.config.from_object(Config)

# login call
login = LoginManager(app=appInstance)
login.login_view = 'login'

# database call
db = SQLAlchemy(app=appInstance)
migrate = Migrate(app=appInstance, db=db)

from app import routes, models