from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import flash

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
    if request.method == 'POST':
        flash("POST Method", "success")
        return render_template("users.html")
    else : 
        flash("GET Method", "success")
        return render_template("users.html")

app.run(debug=True)

