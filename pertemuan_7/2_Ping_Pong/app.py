from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('server_event')
def handle_message(data):
    print('received message : ', data)
    time.sleep(1)
    emit('client_event', 'Hello From Server!')

if __name__ == '__main__':
    socketio.run(app)

    