from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my_event')
def handle_message(data):
    print('received message : ', data)

if __name__ == '__main__':
    socketio.run(app)