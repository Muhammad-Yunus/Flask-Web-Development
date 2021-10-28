from . import app
from . import db

from flask import render_template
from flask import url_for
from flask import request
from flask import flash
from flask import redirect
from flask import session

from sqlalchemy import or_

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
        user = User(name=form.name.data,
                    email=form.email.data,
                    phone=form.phone.data,
                    password=form.password.data,
                    isActive=form.isActive.data)
        db.session.add(user)
        db.session.commit()

        flash("Data submitted successfully!", "success")
        return redirect(url_for("users"))
    else:
        user = User.query.get(id)
        form = UserForm(obj=user)
        return render_template("user.html", form=form)


@app.route('/users', methods=['GET', 'POST'])
def users():

    search_key = "search_users"  # this is can be changes by preference
    if request.method == "POST":
        session[search_key] = request.form.get(search_key)

    page = request.args.get('page')
    page = int(1 if page == None else page)
    baseQuery = User.query.filter(
                                or_(
                                    User.name.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        ),
                                    User.email.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        ),
                                    User.phone.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        )
                                )
                            )

    per_page = 3     # this is can be changes by preference
    destination = 'users'  # this is need to set into current route function name.
    record_list = baseQuery.paginate(page, per_page, error_out=False) 
    min_page = record_list.page - 2 if record_list.page - 2 > 0 else 1
    max_page = min_page + 5 if min_page + 5 <= record_list.pages + 1 else record_list.pages + 1
    record_count = baseQuery.count()

    record_header = ['No', 'Name', 'Email', 'Phone', 'Password', 'Is Active'] # this is can be same as a field in Table
    

    return render_template("user_list.html", 
                            record_list=record_list, 
                            record_header=record_header,
                            record_count=record_count,
                            min_page=min_page,
                            max_page=max_page,
                            destination=destination,
                            search_key=search_key)

                            
