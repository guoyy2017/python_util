#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/19.下午3:51
'''

import sys
import reload_test

a = 3

print a

import time

time.sleep(10)

reload(reload_test)

print a

if __name__ == '__main__':
    pass