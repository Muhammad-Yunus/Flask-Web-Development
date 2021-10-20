from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users', methods=['GET', 'POST'])
def users(): 
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        isAgree = bool(request.form.get('isAgree'))
        
        print("\nPOST Method\n")
        print(name, age, isAgree)

        return render_template("users.html")
    else : 
        print("\nGET Method\n")
        return render_template("users.html")

app.run(debug=True)

