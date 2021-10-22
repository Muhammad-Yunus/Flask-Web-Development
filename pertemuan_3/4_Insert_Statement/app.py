from flask import Flask
import os 

# import Model
from model import db
from model import User, Address

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
    # user_01 = User(
    #                 name = 'John Doe', 
    #                 email='john@mail.com', 
    #                 phone='0812121212', 
    #                 password='john123', 
    #                 isActive=True)
    # user_02 = User(
    #                 name = 'Jasmine',  
    #                 email='jasmine@mail.com', 
    #                 phone='08143434343', 
    #                 password='1234qwerty', 
    #                 isActive=True)
    # db.session.add(user_01)
    # db.session.add(user_02)

    addr = Address(
        description = "Jl Mawar, No. 50",
        city = "Bandung",
        province = "Jawa Barat",
        userId = 3
    )
    db.session.add(addr)
    db.session.commit()
