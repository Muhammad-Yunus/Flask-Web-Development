from app import app 
from app import db 
import os 

if __name__ == '__main__':
    # if database file not exist, create it.
    database_path = app.config['DATABASE_FILE']
    if not os.path.exists(database_path):
        with app.app_context():
            db.create_all()

    # invoke app to run
    app.run()


    