#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/21.下午2:24
'''

import redis
import time

r = redis.Redis('127.0.0.1',6379)

count=1
while True:
    time.sleep(1)
    r.rpush('yyg',count)
    count += 1
    r.rpush('yyg', count)
    count += 1

if __name__ == '__main__':
    pass