from . import app
from . import db

from flask import render_template
from flask import url_for
from flask import request
from flask import flash
from flask import redirect

# import Forms
from .forms import UserForm

# import Model
from .models import User



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users/<int:id>', methods=['GET', 'POST'])
def user(id): 
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
        return redirect(url_for("users"))
    else : 
        user = User.query.get(id)
        form = UserForm(obj=user)
        return render_template("user.html", form=form)

@app.route('/users')
def users(): 
    user_list = User.query.all() 
    user_header = ['No', 'Name', 'Email', 'Phone', 'Password', 'Is Active']
    return render_template("user_list.html", user_list=user_list, user_header=user_header)

