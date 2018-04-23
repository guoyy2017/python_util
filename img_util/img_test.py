#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/23.下午4:46
'''

from gevent import monkey
monkey.patch_socket()
from gevent.pool import Group
import gevent
import requests
import time
import functools
import traceback

def no_error(func):
    @functools.wraps(func)
    def wapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            traceback.print_exc()
            return None
    return wapper
    pass

@no_error
def get_urls():
    # url = ''
    # res = requests.get(url)
    # if res.status_code == requests.codes.ok:
    #     pass
    return ["", "", ""]

@no_error
def get_img(url):
    print 'get begin url %s ' % url
    res = requests.get(url)
    print 'get end url %s ' % url

urls = get_urls()
if urls and len(urls) > 0:
    group = Group()
    start = time.time()
    for url in urls:
        # get_img(url)
        g = gevent.spawn(get_img, url)
        group.add(g)
    group.join()
    end = time.time()
    print 'get cost %f, begin %f, end %f' % (end - start, start , end)

if __name__ == '__main__':
    pass