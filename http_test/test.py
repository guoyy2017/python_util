#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/28.上午10:42
'''

'''
pip install requests
pip install grequests  
Requests + Gevent
并行快速http请求
'''

import grequests

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)
a = grequests.map(rs)
print a


def exception_handler(request, exception):
    print "Request failed"

reqs = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),
    grequests.get('http://fakedomain/'),
    grequests.get('http://httpbin.org/status/500')]
a = grequests.map(reqs, exception_handler=exception_handler)

print a


if __name__ == '__main__':
    pass