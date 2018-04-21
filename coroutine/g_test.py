#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/20.下午6:31
'''

'''
gevent
'''
from gevent import monkey
import gevent
from gevent.pool import Group

monkey.patch_socket()

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

# g1 = gevent.spawn(f, 5)
# g2 = gevent.spawn(f, 5)
# g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()
# gevent.joinall([g1, g2 ,g3])

g1 = gevent.spawn(f, 2)
g = Group()
g.add(g1)
g.join()
# x = g.map(f, xrange(2))

# print x



if __name__ == '__main__':
    pass