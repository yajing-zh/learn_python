#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: fordemo.py
@time:2016/7/31 20:59
"""
x=range(10,20)
for i in x:
    print i

i=0
for item in x:
    print i,item
    i=i+1

#列表常用方法
print "///////////"
for idx,value in enumerate(x):
    print idx,value

#sorted
print "///////22222"
x.extend([-1,-5,-4,-3])
print sorted(x)
print sorted(x,key=abs) #按绝对值排序

#列表解析式
x=range(1,7)
y=[]
#老办法
for i in x:
    y.append(i**2) #对列表中每个元素求平方
print y
#列表解析式
y=[i**2 for i in x]
print y

z=[i**2 if i<3 else i**3 for i in x] #i小于3取平方，大于3取立方
print x
print z


#
x=range(1,10)
#x=range(1,99999999) 此时计算机会挂掉，所以应该使用xrange
y=xrange(1,10) #定义了一个能生成1到10的方法，即一个生成器
print x,y
for i in y:
    print i

#str作用于列表中的每一个元素，且返回一个列表
x=range(1,10)
y=map(str,x)
print y





