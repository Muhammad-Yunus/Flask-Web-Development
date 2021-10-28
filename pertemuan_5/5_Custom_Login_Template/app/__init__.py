from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore

# Create app
app = Flask(__name__)
app.config.from_object('config')

# Create database connection object
db = SQLAlchemy(app)

# Late import models, forms & views
from .models import User, Role
from .views import *

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


