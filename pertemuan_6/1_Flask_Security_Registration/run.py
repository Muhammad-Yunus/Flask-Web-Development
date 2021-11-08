from app import app, db, user_datastore 
import os

if __name__ == '__main__':
    # Create a user to test with
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.import_name, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        with app.app_context():
            db.create_all()
            user_datastore.create_user(email='john@mail.com', password='john123')
            db.session.commit()

    # invoke app 
    app.run()