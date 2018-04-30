#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/28.上午11:13
'''

'''
显示货币格式以及它的数值
'''
from currencies import Currency

currency = Currency('USD')
print currency.get_money_format(13)
print currency.get_money_format('13,2313,33')
print currency.get_money_format('13,231,333')
print currency.get_money_with_currency_format(13.99)

if __name__ == '__main__':
    pass