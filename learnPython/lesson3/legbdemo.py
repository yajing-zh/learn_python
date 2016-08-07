#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: legbdemo.py
@time:2016/8/7 10:43
"""
"""
LEGB原则:
L:local 函数本地
E:enclose 任意上层的嵌套函数
G:global 全局作用域
B:build-in 内置作用域
"""


x='global'

#先找函数内部的
def f1():
    x='local'
    print x
f1()

#函数内部找不到，就在上一层嵌套函数，此处没有嵌套函数，所以就找全局的
def f1():
    #x='local'
    print x
f1()

#本层没找到，就开始找嵌套函数
def outer():
    x="enclose"
    def inner():
        print x
    inner()
outer()

def outer():
    def inner():
        global x #要先声明再使用,且声明为全局作用域
        x+='e'
        print x
    inner()
outer()

#函数也有属性
def f(a,b,c):
    #函数的文档属性
    """

    #自动填充函数参数及返回值
    :param a: int
    :param b: bool
    :param c: string
    :return: int
    """
f.author="zhangyajing"
f.createtime="today"
print f.author,f.createtime
print f.__doc__ #输出函数的文档属性



