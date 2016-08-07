#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: decoratordemo.py
@time:2016/8/7 11:23
"""
#
# def search(keyword):
#     pass
#
# @authorize1 #装饰器
# def order(itemid):
#     pass
#
# #同时满足两个认证方式
# @authorize1
# @authorize2  #可以根据不同的装饰器进行认证
# def pay(orderid):
#     pass
#
# def authorize1(username,password):
#     if username=="zhang" and password=="123456":
#         return True
#     else:
#         return False
#
# #需要修改原有函数，风险较大
# # def order(orderid):
# #     if authorize1("abc",'2345r'):
# #         pass
# #     else:
# #         print "not allow"
#
#

#不带参数的装饰器
def authorize(funname):#要修饰哪个函数，则填写哪个函数名
    def wrapper(*args,**kwargs):#不能预测要装饰的函数的参数是什么样的，索性全部支持
        username=raw_input('username:')
        password=raw_input('password:')
        if username=='zhang' and password=='123456':
            return funname(*args,**kwargs)
        else:
            print "you are not allow"
    return wrapper

def search(keyword1):
    print 'user search product'

#不带参数的装饰器
@authorize #装饰器要在使用之前定义
def order(itemid):
    print 'user order',itemid

def pay(orderid):
    print 'user pay'



order(01)