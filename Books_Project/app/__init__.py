from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Creates the application object as a Flask instance.
app = Flask(__name__)

# Configures application using 'config' file.
app.config.from_object(Config)

# Added database
db = SQLAlchemy(app)

# Initializes database migration structure
migrate = Migrate(app, db)

# Initializes Flask-Login
login = LoginManager(app)
login.login_view = 'login'

# Workaround for circular imports
from app import models, routes