#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/8.上午10:48
'''

'''
https://github.com/glasslion/redlock
'''

from redlock import RedLock,RedLockFactory,ReentrantRedLock
import time

#默认本机redis
# with RedLock('nihao'):
#     time.sleep(10)
#     print 'hello'

#多redis配置 The connection_details parameter expects a list of keyword arguments for initializing Redis clients
# with RedLock('nihao',connection_details=[{'host': '127.0.0.1', 'port': 6379, 'db': 0},]):
#     time.sleep(10)
#     print 'hello'

#重复使用连接
# factory = RedLockFactory(
#     connection_details=[
#         {'host': '127.0.0.1'},
#     ])
#
# with factory.create_lock("nihao"):
#     time.sleep(10)
#     print 'hello'
#
# 直接使用
# lock = RedLock("nihao")
# lock.acquire()
# print 'hello'
# lock.release()

if __name__ == '__main__':
    pass