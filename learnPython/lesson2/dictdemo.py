#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: dictdemo.py
@time:2016/7/31 20:24
"""
#列表是动态的，所以不可hash
#x=[1,2,3,4,5]
#print hash(x)
#字符串是不可变的，所以是可hash的
y='1,2,3,4,5'
print hash(y)

#创建字典对象
z={'name':'zhang','age':30,'sex':'m'}
print z
print z['name']

#不在字典z里会报错
# print z['loc']
#查看loc在不在字典z中
print 'loc' in z

for (k,v) in z.items():
    print k+'='+str(v) #强制类型转换

print z.keys()
print z.values()

#当key loc不存在时，就会自动返回none，防止抛异常，使用场景广泛
print z.get('loc',None)

#直接打印loc对应的value,假如没有，则插入一个，且返回loc的值beijing
print z.setdefault('loc','beijing')

#把m中所有对象加到z中，假如key一样，则更新其value值，此方法无返回值
m={'name':'li','def':2}
z.update(m)
print z

#删除所有元素
print z.clear()





