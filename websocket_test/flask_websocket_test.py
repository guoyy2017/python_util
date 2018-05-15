#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/11.下午3:54
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

socketio.start_background_task() #后台处理线程

@app.route('/')
def index():
    # return render_template('index.html')
    return 'nihao'

@socketio.on('test', namespace='/')
def test_message(message):
    print message
    return 0
    # emit('bbb_response', {'data': 'hello'})

@socketio.on('test2', namespace='/')
def test_message2(message):
    emit('bbb_response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/')
def test_connect():
    print 'nihao'
    # emit('bbb_response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print('Client disconnected')

def change_diff():
    socketio.send('hello',namespace='/')

if __name__ == '__main__':
    socketio.run(app)
    import time
    time.sleep(10)
    change_diff()