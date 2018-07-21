#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/5/2.下午7:18
'''
'''
菜单命令模式
'''

from tty_menu import tty_menu

l = ['a', 'b', 'c']
pos = tty_menu(l, "What is your word?")

print("Your word is %s" % (l[pos]))

for a in l:
    print a

for b in range(1,10):
    print a



if __name__ == '__main__':
    pass