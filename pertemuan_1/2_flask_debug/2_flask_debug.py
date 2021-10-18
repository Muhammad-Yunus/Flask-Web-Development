from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Test Debug Mode</p>"

app.run(debug=True)

