from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)


# Late import so modules can import their dependencies properly
from . import models
from . import forms
from . import views

