from . import app
from . import db

from . import login_required, roles_required, roles_accepted

from . import render_template
from . import url_for
from . import request
from . import flash
from . import redirect
from . import session

from . import or_, and_, not_

# import Forms
from . import UserForm, RoleForm
from . import ActionTable

# import Model
from . import User, Role


# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")


# ############################################################################################### #
#
# USER VIEWS 
#
# ############################################################################################### #

@app.route('/users/<int:id>', methods=['GET', 'POST'])
@login_required
def user(id):
    user = User.query.get(id)
    role_options = [(row.id, row.name) for row in Role.query.all()]
    if request.method == 'POST' :
        form = UserForm(request.form)
        form.role.choices = role_options
        if form.validate_on_submit() :
            user = User() if user is None else user
            user.name = form.name.data
            user.email = form.email.data
            user.phone = form.phone.data
            user.active = form.active.data
            user.roles = [Role.query.get(role_id) for role_id in form.role.data]
            db.session.add(user) if user.id is None else ''
            db.session.commit()

            flash("User submitted successfully!", "success")
            return redirect(url_for("users"))
        else : 
            return render_template("user.html", form=form)
    else:
        form = UserForm(obj=user)
        form.role.choices = role_options
        if user is not None :
            form.role.data = [role.id for role in user.roles]
        return render_template("user.html", form=form)


@app.route('/users', methods=['GET', 'POST'])
@login_required
@roles_required('user')
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

    record_header = ['No', 'Name', 'Email', 'Phone', 'Is Active', 'Confirmed At', 'Action'] # this is can be same as a field in Table
    
    action = ActionTable()

    return render_template("user_list.html", 
                            record_list=record_list, 
                            record_header=record_header,
                            record_count=record_count,
                            min_page=min_page,
                            max_page=max_page,
                            destination=destination,
                            search_key=search_key,
                            action=action)

@app.route('/user/delete/<int:id>', methods=['POST'])
@login_required
@roles_required('admin', 'user')
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully!", "success")
    return redirect(url_for("users"))


@app.route('/user/activate/<int:id>/<int:active>', methods=['POST'])
@login_required
@roles_required('admin', 'user')
def user_activate(id, active):
    user = User.query.get(id)
    user.active = bool(active)
    db.session.commit()
    flash("User %s successfully!" % ("activated" if bool(active) else "deactivated"), "success")
    return redirect(url_for("users"))


# ############################################################################################### #
#
# ROLE VIEWS 
#
# ############################################################################################### #
@app.route('/roles/<int:id>', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def role(id):
    role = Role.query.get(id)
    if request.method == 'POST' :
        form = RoleForm(request.form)
        if form.validate_on_submit() :
            role = Role() if role is None else role
            role.name = form.name.data
            role.description = form.description.data
            db.session.add(role) if role.id is None else ''
            db.session.commit()

            flash("Role submitted successfully!", "success")
            return redirect(url_for("roles"))
        else : 
            return render_template("role.html", form=form)
    else:
        form = RoleForm(obj=role)
        return render_template("role.html", form=form)


@app.route('/roles', methods=['GET', 'POST'])
@login_required
@roles_required('admin')
def roles():

    search_key = "search_roles"  # this is can be changes by preference
    if request.method == "POST":
        session[search_key] = request.form.get(search_key)

    page = request.args.get('page')
    page = int(1 if page == None else page)
    baseQuery = Role.query.filter(
                                or_(
                                    Role.name.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        ),
                                    Role.description.like(
                                        "%{}%".format(session.get(search_key, ''))
                                        )
                                )
                            )

    per_page = 3     # this is can be changes by preference
    destination = 'roles'  # this is need to set into current route function name.
    record_list = baseQuery.paginate(page, per_page, error_out=False) 
    min_page = record_list.page - 2 if record_list.page - 2 > 0 else 1
    max_page = min_page + 5 if min_page + 5 <= record_list.pages + 1 else record_list.pages + 1
    record_count = baseQuery.count()

    record_header = ['No', 'Name', 'Description'] # this is can be same as a field in Table

    return render_template("role_list.html", 
                            record_list=record_list, 
                            record_header=record_header,
                            record_count=record_count,
                            min_page=min_page,
                            max_page=max_page,
                            destination=destination,
                            search_key=search_key)