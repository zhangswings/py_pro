#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
classmates=['Michael', 'Bob', 'Tracy']
print classmates
# len()
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
# print classmates[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print classmates[-1]
print classmates[-2]
print classmates[-3]
