#!/usr/bin/env python
# encoding: utf-8

'''
@author:maidou
@contact:QQ4113291000
@time:2018/4/27.下午5:59
'''

'''
Pyparsing

pip install pyparsing

普通分割标识
分号
semiFlag = Literal(";")
忽略标识
dotFlag = Suppress(Literal("."))
threadID标识
threadID =Word(nums, max=5)
action标识
actionField = Word(alphas)
usecs标识
usecsField = Word(nums, max=8)
class.method标识
clsField = Word(alphas+".")
methodField = Combine("(" + ZeroOrMore(Word(alphas + ";/")) + ")" + Word(alphas + "/") + semiFlag)
signature标识
可以看到跟clsField一致


'''

from pyparsing import Word,alphas

greet = Word( alphas ) + "," + Word( alphas ) + "!"
hello = "Hello, World!"
print hello, "->", greet.parseString( hello )

if __name__ == '__main__':
    pass