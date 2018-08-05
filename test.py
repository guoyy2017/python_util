#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午7:18
'''
'''
菜单命令模式
'''

# from tty_menu import tty_menu
#
# l = ['a', 'b', 'c']
# pos = tty_menu(l, "What is your word?")
#
# print("Your word is %s" % (l[pos]))
#
# for a in l:
#     print a
#
# for b in range(1,10):
#     print a

# from ecc import eccrypt
#
# eccrypt.encrypt()
# eccrypt.decrypt()

import requests
import hashlib
#
# url = 'http://send.supermms.cn/mt.php'
# appkey = '02940e7646'
# appid = '10568'
# mobile = '13451909511'
# modeid = '211022'
# md5 = hashlib.md5()
# md5.update(appkey+appid+mobile)
# sign = md5.hexdigest()
# data = {
#     "appId": appid,
#     "modeId": modeid,
#     "mobile": mobile,
#     "sign": sign,
# }
# print data
# res = requests.post(url, data=data)
# print res.status_code
# print res.text

for i in range(5):
    if i == 3:
        continue
        print i
    else:
        print i



if __name__ == '__main__':
    pass