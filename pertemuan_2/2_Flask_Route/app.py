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

app.run(debug=True)

