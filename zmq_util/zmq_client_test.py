#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/21.上午11:08
'''

'''
经典模式
send_pyobj pyzmq 特有传递python对象
recv_pyobj

pub/sub模式

'''

import zmq

all_topics = []


# import zmq
#
# c = zmq.Context()
#
# s = c.socket(zmq.REQ)
# s.connect("ipc:///tmp/zmq")
# s.send_pyobj("hello")
# msg = s.recv_pyobj()
# print msg
#
# if __name__ == '__main__':
#     pass