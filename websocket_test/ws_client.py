#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/11.下午4:11
'''

from socketIO_client import SocketIO,LoggingNamespace,BaseNamespace

# def on_bbb_response(*args):
#     print('on_bbb_response', args)
#
# with SocketIO('localhost', 5000) as socketIO:
#     print 'hello'
#     socketIO.emit('test', u'狗逼吧')
#     socketIO.on('bbb_response', on_bbb_response)
#     socketIO.wait(seconds=1)

def on_response(*args):
    print('on_response', args)

socket = SocketIO('localhost',5000)
chat = socket.define(BaseNamespace, '/')
print 'hello'
chat.emit('test')
chat.on('bbb_response', on_response)

if __name__ == '__main__':
    pass