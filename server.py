from gevent import monkey
monkey.patch_all()
import json
import threading
import time

from flask import Flask, render_template
from flask.ext.socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def main()
    return render_template('index.html')

def game_play():
    while True:
        time.sleep(1)
        socketio.emit('time',
            {'cur_time': time.asctime()},
            namespace='/dd'
        )

if __name__=='__main__':

    mainprocess = threading.Thread(target=socketio.run, args=(app,))
    mainprocess.start()

    game = threading.Thread(target=game_play)
    game.start()
