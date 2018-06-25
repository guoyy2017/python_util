#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/6/14.上午10:02
'''

'''
本地调用 192.168.0.199:9092
本地调用 192.168.0.199:2181
'''

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='192.168.0.199:9092')
producer.send('hello','nihao')

if __name__ == '__main__':
    pass