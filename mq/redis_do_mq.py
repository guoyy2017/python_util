#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/21.下午2:28
'''

import redis
import time

r = redis.Redis('127.0.0.1',6379)

while True:
    c = r.blpop('yyg',timeout=2)
    print c


if __name__ == '__main__':
    pass