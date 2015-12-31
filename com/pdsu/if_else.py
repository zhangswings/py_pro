#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# 条件判断和循环
age=18
if age>=18:
    print 'your age is ',age
    print 'adult'
else:
    print 'Hey ,little boy'

# if判断条件还可以简写，比如写：
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# x=10
x=0
if x:
    print True
else:
    print False

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
print range(5)
sum=0
for i in range(101):
    sum=sum+i
print sum
# 1050
# while循环
sum1=0
n1=100
while n1>0:
    sum1=sum1+n1
    n1=n1-1
print sum1

# raw_input
# birth=raw_input('please input your birth:')
birth=int(raw_input('please input your birth:'))
# int 数值转换
if birth<2000:
    print '00前'
else:
    print '00后'

