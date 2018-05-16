#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/15.下午7:38
'''

from flask_rq import RQ, Worker, job, get_queue, get_worker
from flask import Flask
app = Flask(__name__)

app.config['RQ_DEFAULT_HOST'] = '127.0.0.1'
app.config['RQ_DEFAULT_PORT'] = 6379
app.config['RQ_DEFAULT_PASSWORD'] = ''
app.config['RQ_DEFAULT_DB'] = 1

RQ(app=app)

@job
def process(i):
    print i

# process.delay(3)

@job('low')
def process2(i):
    print i

# process2.delay(2)

# job = get_queue().enqueue(process)
# job = get_queue('low').enqueue(process)
get_worker().work(True)
get_worker('default','low').work(True)

if __name__ == '__main__':
    pass