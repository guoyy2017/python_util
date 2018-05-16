#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/15.下午7:23
'''

from redis import Redis
import redis
from rq import Queue, Connection, Worker

listen = ['high', 'default', 'low']
conn = redis.from_url('redis://127.0.0.1:6379/1')
with Connection(connection=conn):
    worker = Worker(map(Queue, listen))
    worker.work()



# def test(name):
#     print name
#
# q = Queue('yyg', connection=redis.from_url('redis://127.0.0.1:6379/1'))
# print q.name
#
# # q.enqueue(test, 'yyg')

if __name__ == '__main__':
    pass