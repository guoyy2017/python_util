#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/9.上午11:18
'''

'''
任务处理
'''

from celery import Celery

# app = Celery('tasks', broker='amqp://yyg:seek1234@192.168.0.199:5672//coin')
app = Celery('tasks', broker='redis://127.0.0.1:6379/0')
import time

@app.task
def test():
    time.sleep(10)
    print 'hello'

if __name__ == '__main__':
    pass