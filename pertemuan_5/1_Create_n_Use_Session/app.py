from flask import Flask, session

app = Flask(__name__)
app.config.from_pyfile('config.py')

# views to set session value
@app.route('/set/<key>/<value>')
def set(key, value):
    session[key] = value
    return 'Session, %s : %s' % (key, value)

# views to get session value
@app.route('/get/<key>')
def get(key):
    return 'Value : ' + session.get(key, 'not set')


if __name__ =='__main__':
    app.run()


