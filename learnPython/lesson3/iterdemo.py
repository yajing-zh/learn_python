#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: iterdemo.py
@time:2016/8/7 12:16
"""
import itertools
x=[1,2,3,4]
for i in x:
    print i
for p in itertools.permutations(x,2): #两两元素的排列
    print p

print "**1111**"
for c in itertools.combinations(x,2): #组合
    print c

print "**2222**"
y=['a','b','c']
for p in itertools.product(x,y):#笛卡尔积
    print p

print "**3333**"
piter =itertools.permutations(x,2)#排列
citer=itertools.combinations(x,2)#组合
pditer=itertools.product(x,y)
for i in itertools.chain(piter,citer,pditer):#链接一组迭代器
    print i
