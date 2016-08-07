#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: setdemo.py
@time:2016/7/31 20:45
"""
#集合的参数是列表,且不保证顺序
a=frozenset([1,2,3,4]) #不可变的集合
print a
b=set(range(7,11))
print b

#并集
c=a|b
print c

#是否有交集
print a.isdisjoint(b)

#集合不保证顺序
b.add(1)
print b

#删除
b.discard(10)
# b.remove(10)
print b