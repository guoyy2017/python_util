#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/15.下午8:35
'''

from delay import delayed

@delayed(10)
def foo():
    return 'wow'
import time
time.sleep(10)
res = foo()
print res

if __name__ == '__main__':
    pass