#!/usr/bin/python
# encoding:utf-8

"""
@author:zhangyajing
contact:hebeizhangyajing@126.com
@file: funcdemo1.py
@time:2016/8/7 10:00
"""

def _handleText(txt):
    print txt

def _handleJson(json):
    print json

def _handleHtml(html):
    print html

def decoder(type):
    if type=='txt':
        return _handleText
    elif type=='json':
        return _handleJson
    else:
        return _handleHtml

decoder('html')('<p>this is a html paragraph</p>')
decoder('txt')('<p>this is a txt paragraph</p>')

