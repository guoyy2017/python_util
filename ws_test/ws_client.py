#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/14.下午4:30
'''
from socketIO_client import SocketIO,LoggingNamespace,BaseNamespace

def on_aa(*args):
    print 'nihao '
    print args

socket = SocketIO('localhost',5000)
# chat = socket.define(BaseNamespace, '/')
# print 'hello'
# socket.emit('test','hahao')
socket.once('aa', on_aa)
# socket.emit('test2')
# socket.send('helloo', callback=on_aa)
# socket.send({'helo':'helo'})
socket.wait_for_callbacks(seconds=20)
socket.wait(10)
# socket.once('aa', on_aa)
# import time
# time.sleep(20)



if __name__ == '__main__':
    pass