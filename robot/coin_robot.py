#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/26.下午1:51
'''

'''
币种机器人
'''
from wxbot import WXBot

class CoinRobot(WXBot):
    
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            content = msg['content']['data'].strip()
            if len(content) < 10:
                content = content.upper()
                if content in symbols:
                    info = self.deal_symbol(content)
                    self.send_msg_by_uid(info, msg['user']['id'])
        elif msg['msg_type_id'] == 3 and msg['content']['type'] == 0:
            pass


if __name__ == '__main__':
    pass