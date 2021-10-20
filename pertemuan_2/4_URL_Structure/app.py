from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users/<name>')
def users(name): 
    return "<p> Name : %s <p>" % name

@app.route('/users/<name>/setting')
def user_setting(name): 
    return "<p> User setting page for %s <p>" % name

@app.route('/users/<name>/setting/<email>')
def user_setting_email(name, email): 
    return "<p> User setting page for %s with email %s <p>" % (name, email)



app.run(debug=True)

