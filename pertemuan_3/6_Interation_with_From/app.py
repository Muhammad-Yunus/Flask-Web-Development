from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import flash
import os 

# import Forms
from forms import UserForm

# import Model
from model import db
from model import User

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users/<int:id>', methods=['GET', 'POST'])
def users(id): 
    if request.method == 'POST':
        form = UserForm(request.form)
        user = User(name = form.name.data,
                    email = form.email.data,
                    phone = form.phone.data,
                    password = form.password.data, 
                    isActive = form.isActive.data) 
        db.session.add(user)
        db.session.commit()
        
        flash("Data submitted successfully!", "success")
    else : 
        user = User.query.get(id)
        form = UserForm(obj=user)
    return render_template("users.html", form=form)


if __name__ == "__main__":
    # if database file not exist, create it.
    database_path = app.config['DATABASE_FILE']
    if not os.path.exists(database_path):
        with app.app_context():
            db.create_all()

    app.run(debug=True)

