#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: wordcount.py
@time:2016/7/31 23:00
"""
# -*- coding: utf-8 -*-
import os, sys
from lesson2.sortdemo import mysort

info = os.getcwd()  # 获取当前文件名称
fin = open(u'c:/a.txt')

info = fin.read()
alist = info.split(' ')  # 将文章按照空格划分开

#print alist
for i in alist:
    if i=='':
        alist.remove(i)
print mysort(alist,'sort',True) #倒序排列
print mysort(alist,'sort',False)#正序排列
fin.close()
