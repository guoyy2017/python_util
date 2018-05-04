#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/4.下午2:03
'''

'''
灰度测试用
pip install regal
'''

from regal import BaseInfo

#combine 希望以每组多少台服务器作为一组,进行用户群B的分流
ab = BaseInfo(
    version_host={
        'version-1.0':'192.168.0.1,192.168.0.2,192.168.0.3,192.168.0.4',
        'version-2.0':'192.168.0.5,192.168.0.6,192.168.0.7,192.168.0.8',
    }
              ,combine=2,
              schedule=2)

# grouping() 进行分组
# smart_grouping = ab.grouping()
# grouping()方法还提供了priority_name参数，当需要在多版本发布的时候，设置优先级，指定你需要优先发布的'版本名'
smart_grouping = ab.grouping(priority_name='version-2.0')

print smart_grouping.result

for i in smart_grouping.iter_dict():
    print i

if __name__ == '__main__':
    pass