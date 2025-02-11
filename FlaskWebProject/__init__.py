"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, user_logged_in, user_login_failed
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
app.logger.addHandler(stream_handler)
  
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Log successful login attempts
@user_logged_in.connect_via(app)
def log_successful_login(sender, user):
    app.logger.info(f"User {user.username} logged in successfully.")

# Log invalid login attempts
@user_login_failed.connect_via(app)
def log_invalid_login(sender, user):
    app.logger.warning("Invalid login attempt.")

import FlaskWebProject.views
