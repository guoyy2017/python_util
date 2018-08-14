#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 上午11:35
# @Author  : maidou
# @Site    : 
# @File    : simple_service.py
# @Software: PyCharm

'''
service 定义
nameko run module:[ServiceClass]
ServiceRunner 是多个服务容器的简单包装
'''
from nameko.rpc import rpc

class SimpleService:
    name = "simple_service"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
