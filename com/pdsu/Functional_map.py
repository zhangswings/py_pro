#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Python内建了map()和reduce()函数。
如果你读过Google的那篇大名鼎鼎的论文“MapReduce: Simplified Data Processing on Large Clusters”，你就能大概明白map/reduce的概念。
我们先看map。map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00141861202544241651579c69d4399a9aa135afef28c44000
'''
def f(x):
    return x*x
print f(2)
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
map()传入的第一个参数是f，即函数对象本身。
你可能会想，不需要map()函数，写一个循环，也可以计算出结果：
'''
L=[]
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print L
