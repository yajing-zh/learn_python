#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: embeddemo.py
@time:2016/8/7 11:19
"""

def outer():
    print "in outer function"
    def inner():
        print "in inner function"
    return inner
x=outer()
x() #触发内部函数的执行
# print outer()