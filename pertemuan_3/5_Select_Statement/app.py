from flask import Flask
import os 

# import Model
from model import db
from model import User

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


# if database file not exist, create it.
database_path = app.config['DATABASE_FILE']
if not os.path.exists(database_path):
    with app.app_context():
        db.create_all()

    
# Insert Data
with app.app_context():
    user_01 = User(
                    name = 'John Doe', 
                    email='john@mail.com', 
                    phone='0812121212', 
                    password='john123', 
                    isActive=True)
    user_02 = User(
                    name = 'Jasmine',  
                    email='jasmine@mail.com', 
                    phone='08143434343', 
                    password='1234qwerty', 
                    isActive=True)
    db.session.add(user_01)
    db.session.add(user_02)
    db.session.commit()


# Select Data
with app.app_context():

    # Query all data 
    users = User.query.all()

    # Query the first record 
    user = User.query.first()

    # Query with filter by name if match
    user = User.query.filter_by(name = 'Jasmine').first()

    # Query with filter with complex expression
    user = User.query.filter(User.name.contains('John')).first()
    
    # Query with order
    users = User.query.order_by(User.name).all()

    # Query with limit
    users = User.query.limit(1).all()

    # Query by Id
    users = User.query.get(1)

