#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: strdemo.py
@time:2016/7/31 20:07
"""

x = 'hello world'

#字符串类似元组，内容不可修改
#x[0]='z'
y = x + 'e'
print y

#单引号
x = 'hello \'world'
print x

#双引号
x = "hello \"world"
print x

#乘法
print x*3

#.join方法,拼接
x=['hello','world','python']
print ' '.join(x)
print ','.join(x)







