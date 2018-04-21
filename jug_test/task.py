#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/16.下午4:27
'''

'''
jug 测试内容
'''

from jug import TaskGenerator

import time
import os,sys

@TaskGenerator
def is_prime(n):
    print '任务 %s' % n
    time.sleep(1)
    ltime = int(time.time())
    print ltime
    time.sleep(1)
    return True

plist = [1,2,3,4,5,6,7,8,9,10,'w1','w2','w3','w4','w5','w6','d1','d2','d3','d4','d5','d6']
primes100 = map(is_prime, plist)
print 'o'

if __name__ == '__main__':
    pass