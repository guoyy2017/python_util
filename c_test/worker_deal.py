#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/16.下午1:57
'''

from celery import Celery

brokers = 'redis://127.0.0.1:6379/3'
backend = 'redis://127.0.0.1:6379/4'
app = Celery('tasks', backend=backend, broker=brokers)

@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    pass