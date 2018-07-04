#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/14.下午4:30
'''

from leveldb import LevelDB

db = LevelDB('./data')
db.Put('nohao','wobuxing')
print db.Get('nihao')