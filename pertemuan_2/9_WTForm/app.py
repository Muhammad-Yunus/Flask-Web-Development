from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import flash

# import Forms
from forms import UserForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty123'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users', methods=['GET', 'POST'])
def users(): 
    form = UserForm(request.form)
    if request.method == 'POST':
        
        print("\nPOST Method\n")
        print(form.name.data, form.email.data, form.password.data, form.accept_tos.data)
        
        flash("Data submitted successfully!", "success")
    return render_template("users.html", form=form)

app.run(debug=True)

