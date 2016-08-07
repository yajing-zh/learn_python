#!/usr/bin/python
# encoding:utf-8

from math import exp

def sigmod(x):
    y=1/(1.0+exp(-x))
    return y

if __name__=='__main__':
    sigmod(0)
    print sigmod(0)
