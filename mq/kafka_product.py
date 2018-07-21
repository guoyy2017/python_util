#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午3:37
# @Author  : maidou
# @Site    : 
# @File    : kafka_product.py
# @Software: PyCharm

from kafka import KafkaProducer

# producer = KafkaProducer(bootstrap_servers='172.16.1.14:9092')
producer = KafkaProducer(zookeepr='172.16.1.14:9092')
for _ in range(10):
    producer.send('world', b'some_message_bytes')