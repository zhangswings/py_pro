#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
def fun(a):
	b=set(a)
	c={}
	for i in b:
		c[i] = 0
	for i in a:
		c[i]+=1
	return c

a="java:统计字符串中英文字母,空格,数字和其他字符出现的次数!".decode("utf-8")
result=fun(a)
for i in result:
	print i+":"+str(result[i])