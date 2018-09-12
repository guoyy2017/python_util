#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/11 下午10:12
# @Author  : maidou
# @Site    : 
# @File    : abtest2.py
# @Software: PyCharm

import fire
import gevent
from gevent import monkey
import logging
import time
import requests
import threadpool
from threadpool import ThreadPool

monkey.patch_socket

#console log
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                # filename='warn.log',
                # filemode='w'
                    )

'''
执行task 方法如下 python abtest2.py test --conf conf.txt --c 10 --n 300 -k url
默认 --c 5 --n 10 如果配置了conf url 不适用，如果没有conf 没有url会报错
'''

class DEAL():

    def __init__(self):
        self._results = []
        self._keeplive = False
        pass

    def test(self, *args, **kwargs):
        threads = 5
        num = 10
        if "c" in kwargs:
            threads = int(kwargs['c'])
        if "n" in kwargs:
            num = int(kwargs['n'])
        if "conf" in kwargs:
            conf = kwargs['conf']
            with open(conf) as f:
                urls = []
                for l in f.readlines():
                    urls.append(l.strip())
            logging.info(urls)
            if len(args) > 0 and '-k' == args[0]:
                self._keeplive = True
            self._run(urls, None, threads, num)
        elif len(args) > 0:
            if '-k' == args[0]:
                self._keeplive = True
                url = args[1]
            else:
                url = args[0]
            self._run(None, url, threads, num)
        pass

    def _run(self, urls, url, threads, num):
        pool = ThreadPool(threads)
        params = []
        if url:
            [params.append([]) for j in range(threads)]
            for i in range(num):
                params[i % threads].append(url)
                # params.append(url)
        else:
            l = len(urls)
            [params.append([]) for j in range(threads)]
            for i in range(num):
                params[i % threads].append(urls[i % l])
                # params.append(urls[i % l])
        begin = time.time()
        requests = threadpool.makeRequests(self._gevent_deal, params)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        pool.dismissWorkers(threads)
        end = time.time()
        logging.info("all cost %f s" % (end-begin))
        self._deal_results()
        pass

    def _deal_results(self):
        num = len(self._results)
        logging.info(u'请求数据量 %d' % num)
        self._results.sort(cmp=lambda x,y:-1 if x[1] < y[1] else 1)
        success_num = 0
        for r in self._results:
            if r[0]:
                success_num += 1
        logging.info(u'成功率 %f %%' % (100 * success_num / num))
        logging.info(u'50%% finish %f s' % (self._results[int(num * 0.5 - 1)][1]))
        logging.info(u'60%% finish %f s' % (self._results[int(num * 0.6 - 1)][1]))
        logging.info(u'70%% finish %f s' % (self._results[int(num * 0.7 - 1)][1]))
        logging.info(u'80%% finish %f s' % (self._results[int(num * 0.8 - 1)][1]))
        logging.info(u'90%% finish %f s' % (self._results[int(num * 0.9 - 1)][1]))
        logging.info(u'100%% finish %f s' % (self._results[int(num  - 1)][1]))
        pass

    def _gevent_deal(self, urls):
        runs = []
        if self._keeplive:
            r = requests.session()
        else:
            r = requests
        for url in urls:
            runs.append(gevent.spawn(self._get_url, r, url))
        gevent.joinall(runs)
        pass

    def _get_url(self, r, url):
        begin = time.time()
        success = False
        try:
            req = r.get(url)
            if req.status_code == requests.codes.ok:
                success = True
        except:
            pass
        end = time.time()
        self._results.append([success, end-begin])
        pass

    pass

if __name__ == '__main__':
    fire.Fire(DEAL)