#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/11.上午10:42
'''

import requests

url = "https://oapi.dingtalk.com/robot/send?access_token=759a361ccc4143dba3d9d23aa13ce56eef51c8c6fbb9d25e354521d2151a667b"
data = {
     "msgtype": "text",
     "text": {
         "content": "我就是我,  @1825718XXXX 是不一样的烟火"
     },
     "at": {
         "atMobiles": [
             "13451909511"
         ],
         "isAtAll": True
     }
 }
requests.post(url=url, json=data)

if __name__ == '__main__':
    pass