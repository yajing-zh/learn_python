#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: searchWeek.py
@time:2016/8/7 12:30
"""
def month_to_day(c):
    dic={11:334,10:304,9:273,8:243,7:212,6:181,5:151,4:120,3:90,2:59,1:31}
    return dic[c]

def show(day):
    day=day%7
    week={0:'星期日',1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六'}
    return week[day]

def searchWeek(year,month):
    a=year-1900 #过了几年
    b=a/4 #a中有几年是瑞年
    c=month-1 #过了几个月
    c=month_to_day(c) #把月份转成天数
    if a%4==0 and a!=0:#判断输入的年份是不是闰年
        b=b-1
        c=c+1
        d=(a-b)*365+b*366+c;
    else:
        d=(a-b)*365+b*366+c+day;
        show(d)

print month_to_day(2)
print show(20)



