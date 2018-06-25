#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/12.下午1:40
'''
'''
工作进程
'''
import random, time, Queue
from multiprocessing.managers import BaseManager


def start_worker(host, port, authkey):
    # 由于这个BaseManager只从网络上获取queue，所以注册时只提供名字
    BaseManager.register('get_task_queue')
    BaseManager.register('get_result_queue')
    print ('Connect to server %s' % host)
    # 注意，端口port和验证码authkey必须和manager服务器设置的完全一致
    worker = BaseManager(address=(host, port), authkey=authkey)
    # 链接到manager服务器
    worker.connect()
    return worker


def get_queue(worker):
    task = worker.get_task_queue()
    result = worker.get_result_queue()
    # 从task队列取数据，并添加到result队列中
    while 1:
        if task.empty():
            time.sleep(1)
            continue
        n = task.get(timeout=1)
        print ('worker get %d' % n)
        result.put(n)
        time.sleep(1)

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000
    authkey = 'abc'
    # 启动worker
    worker = start_worker(host, port, authkey)
    # 获取队列
    get_queue(worker)