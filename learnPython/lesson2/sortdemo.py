#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: sortdemo.py
@time:2016/7/31 21:56
"""
"""
 1.自己实现一个排序算法，不能使用python内置的sorted和sort，具体哪种排序算法不限；
函数接口：mysort(data)
可选部分：【 对于有一定基础的同学，可以考虑扩展接口如下
               mysort(data,key=somefunc,reveresed=True|False）
                支持自定义比较函数，比如按照sin(x)或者abs(x)结果排序这样；
                支持正序或者逆序排序；】
2.实现测试用例；
3.实现wordcount，自己找一篇英文文章或者句子，统计每个单词出现次数，并使用1中的排序算法输出排序后
的结果；
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





