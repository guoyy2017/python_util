#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 下午3:51
# @Author  : maidou
# @Site    : 
# @File    : kafka_consumer.py
# @Software: PyCharm

from kafka import KafkaConsumer


consumer=KafkaConsumer('world',group_id='consumer-20171017',bootstrap_servers=['172.16.1.14:9092'])
for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" %(msg.topic,msg.partition,msg.offset,msg.key,msg.value)
