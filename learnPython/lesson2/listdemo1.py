# #!/usr/bin/python
# # encoding:utf-8
#
# """
# @author:zhangyajing
# contact:hebeizhangyajing@126.com
# @file: listdemo1.py
# @time:2016/7/31 19:42
# """

# x = [1,2,3,4]
# y = {}
# print x
# print y
#
# #追加
# x.append(5)
# print x
#
# #扩展
# x.extend([6,7,8])
# print x
#
# #删除
# del x[0]
# print x
#
# #加法和乘法
# y = [9,10]
# print x+y
# print y * 3
#
# #切片操作[begin:end:step]
# 左闭右开，不包含右边界，begin，end可以是负数，step表示步幅和方向
x = range(1,20)
print x

#倒序
y = x[::-1]
print y

#切片操作自动解决越界问题
print x[2:100:3]

# 越界
#print x[20]













