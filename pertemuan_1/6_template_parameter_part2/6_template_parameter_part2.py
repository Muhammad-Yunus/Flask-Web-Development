from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    User={}
    User["name"] = "John Doe"
    User["age"] = 28
    User["address"] = "Jakarta, Indonesia"


    hobbies = ["traveling", "photography", "cooking", "swimming"]
    return render_template("index.html", User=User, hobbies=hobbies)

@app.route('/about')
def hello():
    return render_template("about.html",)

app.run()

