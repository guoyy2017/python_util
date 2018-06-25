#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/14.上午10:15
'''

'''
客户端 消费者
'''

from kafka import KafkaConsumer

consumer=KafkaConsumer('world',group_id='consumer-20171017',bootstrap_servers=['192.168.120.11:9092'])

for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)

if __name__ == '__main__':
    pass