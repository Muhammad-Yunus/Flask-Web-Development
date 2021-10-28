import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db.init_app(app)

sess = Session(app)
app.config['SESSION_SQLALCHEMY'] = db

# views to set session value
@app.route('/set/<key>/<value>')
def set(key, value):
    session[key] = value
    return 'Session, %s : %s' % (key, value)

# views to get session value
@app.route('/get/<key>')
def get(key):
    return 'Value : ' + session.get(key, 'not set')


if __name__ =='__main__':
    # if database file not exist, create it.
    database_path = app.config['DATABASE_FILE']
    if not os.path.exists(database_path):
        sess.app.session_interface.db.create_all()

    # invoke app
    app.run()


