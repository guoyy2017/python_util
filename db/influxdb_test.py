#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 下午2:43
# @Author  : maidou
# @Site    : 
# @File    : influxdb_test.py
# @Software: PyCharm

from influxdb import InfluxDBClient

#client = InfluxDBClient("172.16.1.14", 8086, "admin", "admin" , "yyg")
client = InfluxDBClient("115.231.102.197", 8086, "admin", "admin" , "yyg")

points = [{'measurement': 'win',
                 'tags': {'cpu': 'i7-7700H0'},
                 'fields': {'cpu_info_user': 0,
                            'cpu_info_system': 0,
                            'cpu_info_idle': 0,
                            'cpu_info_interrupt': 0,
                            'cpu_info_dpc': 0}}]
# client.write_points(points)

# q = client.query('select * from win')
q = client.query('show series from win')
print q
# client.query('drop measurement win')