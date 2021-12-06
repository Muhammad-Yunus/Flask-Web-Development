import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_security import SQLAlchemyUserDatastore
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_mqtt import Mqtt

# Create app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Create database connection object
db = SQLAlchemy(app)

# Create Mail object
mail = Mail()
mail.init_app(app)

# Create MQTT Object
mqtt = Mqtt()
mqtt.init_app(app)

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

# Late import views for API
from app.views.api import *

# Late import views for MQTT Subscriber
from app.views.mqtt_sub import *

# Late Import models and forms Filter Date Dashboard
from app.models.filter_date import *
from app.forms._action import *

