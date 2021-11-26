from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_socketio import SocketIO

# Create app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Create database connection object
db = SQLAlchemy(app)

# Create Mail object
mail = Mail()
mail.init_app(app)

# Create SocketIO Instance
socketio = SocketIO(app, async_mode="eventlet")


# Late import views (Common)
from app.views.home import *
from app.views.about import *

# Late import models, forms & views (User)
from app.models.user import User, Role
from app.views.user import *
from app.forms.user import *

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Late import models, forms & views (Sensor)
from app.models.sensor import Sensor
from app.views.sensor import *
from app.forms.sensor import *