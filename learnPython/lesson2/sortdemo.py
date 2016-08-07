#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: sortdemo.py
@time:2016/7/31 21:56
"""

def mysort(array,key,reveresed):
    if key == 'abs':
        x = map(abs, array)  # 对于Python3.x需要用list函数对map的返回值转换为列表

    if key=='sort':
        x=array

    for i in range(len(x))[::-1]:
     for j in range(i):
         if reveresed: #从大到小
             if x[j]<x[j+1]:
                x[j], x[j + 1] = x[j + 1], x[j]
         else: #从小到大
             if x[j]>x[j+1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

if __name__=='__main__':
    x = [5, 2, -1, 10, 7, 4, 8, -3]

   # y = map(abs, x)  # 对于Python3.x需要用list函数对map的返回值转换为列表
    # print y
    print mysort(x,'abs',True)
    print mysort(x,'abs',False)
    print mysort(x,'sort',True)
    print mysort(x,'sort',False)





