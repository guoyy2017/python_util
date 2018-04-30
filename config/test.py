#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/28.上午10:51
'''

'''
解决读取环境变量问题
将设置和代码完全隔离
pip install python-decouple 
Decouple支持两种类型：.ini文件和.env 文件

https://www.cnblogs.com/leeronggui/p/5380050.html

Decouple 有5个类：

Config
检索配置文件所在的位置
RepositoryIni
按照顺序从os.environ，ini文件中读取值
注意：从3.0开始unix环境变量高于配置文件变量
RepositoryEnv
按照顺序从os.environ，.env文件中读取值
注意：从3.0开始unix环境变量高于配置文件变量
RepositoryShell
只是从os.environ中获取环境变量
AutoConfig
检查你使用的配置
它将从你的配置模块路径递归的搜索settings.ini或者.env文件
'''

from decouple import config

if __name__ == '__main__':
    pass