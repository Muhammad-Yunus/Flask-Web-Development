from flask import Flask

# import Model
from model import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# Creting Database & Model
with app.app_context():
    db.create_all()

    

