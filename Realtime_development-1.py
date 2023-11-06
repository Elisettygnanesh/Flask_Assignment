from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thesecretkeyisspecial'  
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('Realtime_development-1.html')

@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=8000)
