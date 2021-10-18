from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "John Doe"
    age = 28
    address = "Jakarta, Indonesia"
    return render_template("index.html", name=name, 
                                        age=age, 
                                        address=address)

@app.route('/about')
def hello():
    return render_template("about.html",)

app.run()

