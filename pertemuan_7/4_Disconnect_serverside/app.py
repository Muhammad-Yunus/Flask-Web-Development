from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit, disconnect
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

call = 0

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('server_event')
def handle_message(data):
    global call
    print('received message : ', data)
    time.sleep(1)
    call += 1
    if call > 10 : 
        print('Communication call exceeded! disconnect from server.')
        disconnect()
    else : 
        emit('client_event', 'Hello From Server!')

@socketio.on('connect')
def connect_handler():
    print("Client Connected!")

@socketio.on('disconnect')
def disconnect_handler():
    print("Client Disconnected!")

if __name__ == '__main__':
    socketio.run(app)