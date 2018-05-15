#!/usr/bin/env python
# encoding: utf-8

'''
send()用于非自定义的事件而emit()用于自定义的事件中
socketio.send()和socketio.emit()可以用来向所有用户发送广播
join_room() 和leave_room() 用户分组
send emit 执行房间发送 room='room'
@author:maidou
@contact:QQ4113291000
@time:2018/5/14.下午4:27
'''

from flask import Flask, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room, disconnect, rooms
import time
app = Flask(__name__)
socketIO = SocketIO(app=app, async=None)

def send_to_clients():
    while True:
        # time.sleep(1)
        socketIO.sleep(1)
        # print 111
        socketIO.emit('aa', 'hahhaah')

thread = None
@socketIO.on('connect', namespace='/')
def connect():
    print 'connect id %s' % request.sid
    global thread
    if thread is None:
        print 0
        thread = socketIO.start_background_task(target=send_to_clients)
        print 111
    # socketIO.start_background_task(target=send_to_clients)
    # return False
    pass

@socketIO.on('test2', namespace='/')
def test2():
    global count
    print 'test id %s' % request.sid
    leave_room(request.sid)
    count += 1
    print rooms()
    emit('aa')

@socketIO.on('disconnect', namespace='/')
def disconnect():
    send('level',room=rooms()[0])
    print rooms()
    pass

count = 0
@socketIO.on('test', namespace='/')
def test(data):
    global count
    print data
    print 'test id %s' % request.sid
    join_room(str(count))
    count += 1
    print rooms()
    emit('aa')

#服务端未命名事件处理函数
@socketIO.on('message')
def message(message):
    # raise RuntimeError()
    print 'msg %s' % message
    emit('aa', 'helloo', broadcast=True) #广播
    return message
    pass

#使用了字符串消息，下面的例子展示如何使用json格式的消息
@socketIO.on('json')
def json(json):
    print 'json %s' % str(json)
    pass

@socketIO.on_error()        # Handles the default namespace
def error_handler(e):
    print '/ error'
    print request.event["message"]  # "my error event"
    print request.event["args"]  # (data,)
    pass
@socketIO.on_error('/chat') # handles the '/chat' namespace
def error_handler_chat(e):
    pass
@socketIO.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print 'all error'
    pass



if __name__ == '__main__':
    socketIO.run(app, debug=True)
    pass