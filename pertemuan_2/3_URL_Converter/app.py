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

@app.route('/post/<int:post_id>')
def post(post_id): 
    return "<p> Post Id : %d <p>" % post_id

@app.route('/circle/<float:radius>')
def circle(radius): 
    return "<p> Perimeter of circel with radius %.2f is %.2f. <p>" % (radius, 3.14*radius**2)


app.run(debug=True)

