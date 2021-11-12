from app import app, db, user_datastore, Role 
import os

if __name__ == '__main__':
    # Create a user to test with
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.import_name, app.config['DATABASE_FILE'])
    
    with app.app_context():
        db.create_all()
        db.session.commit()
        
        if Role.query.count() == 0 :
            # add default role
            user_role = Role(name='user')
            admin_role = Role(name='admin')
            db.session.add(user_role)
            db.session.add(admin_role)
            db.session.commit()
            
            # default user
            user_datastore.create_user(
                name='John Doe',
                email='john@mail.com', 
                password='john123', 
                roles=[user_role, admin_role])
            user_datastore.create_user(
                name='Jasmine',
                email='jasmine@mail.com', 
                password='jasmine123', 
                roles=[user_role])
            db.session.commit()

    # invoke app 
    app.run()
