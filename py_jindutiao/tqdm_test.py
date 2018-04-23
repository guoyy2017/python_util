#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:18/4/23.下午8:30
'''

'''
python console 进度条
pip install tqdm

函数有 tqdm trange
for i in tqdm(range(1000)):

for i in trange(1000):

qar = tqdm(range(1000))
手动控制更新
qar.update(10)
'''

from tqdm import *
import time
import os

# for i in tqdm(range(1000)):
#     # print i
#     time.sleep(0.1)

for  i in range(1000):
    print i,
    time.sleep(0.1)
    print '\r',


if __name__ == '__main__':
    pass