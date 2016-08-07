#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: turpledemo.py
@time:2016/7/31 20:01
"""

x = (1,3,5)
print x[0],x[1]

#元组不能增加
#能同时返回三个值
def add(x,y):
    return x,y,x+y
print add(10,20)

#返回的result是一个元组
#典型的使用场景
result = add(10,20)
print result,result[2],result[0],result[1]

x,y,z=add(10,20)
print x,y,z

