#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/20.下午1:57
'''

'''
pip install schedule

schedule.every(10).minutes.do(job)

schedule.run_pending()


'''

import schedule
import time

def job():
    print 11

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    pass