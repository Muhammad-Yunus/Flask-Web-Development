from flask import render_template
from flask_security import login_required

from . import app
from . import db



# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')