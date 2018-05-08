#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/8.下午4:19
'''

'''
Celery是Python开发的分布式任务调度模块
pip install Celery
http://docs.celeryproject.org/ 文档地址

http://python.jobbole.com/87238/

概念
brokers 中文意思为中间人 brokers 有 rabbitmq、redis、Zookeeper
backend 有 redis、Memcached 甚至常用的数据都可以
Workers Celery 中的工作者，类似与生产/消费模型中的消费者，其从队列中取出任务并执行
Tasks 队列中进行的任务 由用户、触发器或其他操作将任务入队

执行
celery -A tasks worker --loglevel=info

触发任务

'''

from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


@app.task  # 普通函数装饰为 celery task
def add(x, y):
    return x + y

#触发任务啦
import  time
result = add.delay(4, 4) #不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(1)
print 'task done: {0}'.format(result.get())
# delay 返回的是一个 AsyncResult 对象，里面存的就是一个异步的结果，当任务完成时result.ready() 为 true，然后用 result.get() 取结果即可。


#复写 task 的 on_failure、on_success
from celery import Task
class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print 'task done: {0}'.format(retval)
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print 'task fail, reason: {0}'.format(exc)
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask)
def add(x, y):
    return x + y
if __name__ == '__main__':
    pass