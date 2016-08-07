#!/usr/bin/python
# encoding: utf-8
def hello():
    print "i am in demo1"

def add(x,y):
    return x+y
#可以把测试代码写到main中，这样别的类调用此类时，也不会执行main函数
if __name__=='__main__':
    hello()
    a=10
    b="hello"
    c='''hello1
    hello2
    helllo3
    '''
    d,e,f=5,'world',True
    print a,b,c,d,e,f
