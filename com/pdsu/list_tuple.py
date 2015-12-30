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
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append("Adam")
print classmates
# insert( )
classmates.insert(1,'Tom')
print classmates
# 删除 pop( )
classmates.pop(2)
print classmates
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1]='swings'
print classmates
# list里面的元素的数据类型也可以不同，比如 ['Michael', 'swings', 'Tracy', 'Adam', 120]
classmates.append(120)
print classmates


# list元素也可以是另一个list，比如
s = ['python', 'java', ['asp', 'php'], 'scheme']
print s
print len(s)
# 要注意s只有4个元素，其中s[2]又是一个list，如果拆开写就更容易理解了：
p= ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print s
print s[2]
# 要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
print s[2][1]
L=[]
print len(L)