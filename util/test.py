#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 上午9:59
# @Author  : maidou
# @Site    : 
# @File    : test.py
# @Software: PyCharm

# import random
# from tenacity import retry,stop_after_attempt,stop_after_delay,wait_random
#
#
# @retry(stop=stop_after_delay(2), wait=wait_random(2))
# def do_something_unreliable():
#     if random.randint(0, 10) > 1:
#         print 'error'
#         raise IOError("Broken sauce, everything is hosed!!!111one")
#     else:
#         return "Awesome sauce!"
#
# print(do_something_unreliable())

import requests,time,hashlib

appKey = "TESTAPP"
custId = "20"
modeId = "20"
mobile = "13451909511"
ts = int(time.time())
appSecret = "123456"
h = hashlib.md5()
h.update("%s%s%s%s" % (modeId, ts, appKey, appSecret))
sign = h.hexdigest()
url = "http://172.16.1.14:8888/testVsms?appKey=%s&custId=%s&modeId=%s&mobile=%s&ts=%s&sign=%s" % (appKey, custId, modeId, mobile, ts, sign);
print url
resp = requests.get(url=url)
print resp.text
