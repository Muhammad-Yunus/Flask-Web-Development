from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_mail import Mail

# Create app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Create database connection object
db = SQLAlchemy(app)

# Create Mail object
mail = Mail()
mail.init_app(app)

# Late import models, forms & views
from app.models.user import User, Role
from app.views.user import *
from app.forms.user import *

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
