from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", about_URL=url_for('about'))

@app.route('/about')
def about():
    return render_template("about.html", home_URL=url_for('index'))

app.run()

