from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')

name_space = '/dcenter'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/push')
def push_once():
    event_name = 'dcenter'
    broadcasted_data = {'data': "test message!"}
    socketio.emit(event_name, broadcasted_data, namespace=name_space)
    return 'done!'

@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')

@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')

# @socketio.on('my_event', namespace=name_space)
# def mtest_message(message):
#     print(message)
#     emit('my_response',
#          {'data': message['data'], 'count': 1})

if __name__ == '__main__':

    socketio.run(app, host='127.0.0.1', port=5000, debug=True)