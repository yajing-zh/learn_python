#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: funcdemo2.py
@time:2016/8/7 10:17
"""

def add(a,b):
    return a+b;

def add(*args):
    return sum(args)*2

#同名函数后边的会自动覆盖前边的
print add(10,20)

def  add(a,b,c):
    return a+b+c

#位置参数
print add(10,20,30)

#关键字形参
print add(10,c=20,b=40)

x=[1,2,5]
print add(x[0],x[1],x[2])
print add(*x)

y={'a':10,'b':20,'c':30}
print add(y['a'],y['b'],y['c'])
print add(**y) #key必须与形参名字保持一致

#*代表参数是一个列表
def add(*args):
    return sum(args)

print add(10,2,3)

#**代表参数是一个字典
def add(**kwargs):
    return sum(kwargs.values())
print add(a=10,b=2,c=4)

def add(*args,**kwargs):
    return sum(args)+sum(kwargs.values())
print add(1,2,a=3,b=4)

#函数传递的是指针
x=[1,2,3,4]
def f(a):
    a[2]='hello'
f(x)
print x




