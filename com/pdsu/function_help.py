#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# 绝对值
print abs(100)
print abs(-100)
# abs(1,2) 传入错误的参数
# TypeError: abs() takes exactly one argument (2 given)
# 比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
print cmp(1,2)


# 数据类型转换
print int('123')
print int(12.34)
print float('12.34')
print str('123')
print unicode(1000)
print bool(1)
print bool(0)

# 定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print my_abs(-15)

# 空函数
#
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
#
# def nop():
#     pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
#
# pass还可以用在其他语句里，比如：
#
# if age >= 18:
#     pass
# 缺少了pass，代码运行就会有语法错误。

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# 但是如果参数类型不对，Python解释器就无法帮我们检查。
def my2_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# my2_abs(w)
import math
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print move(100,100,60,math.pi/6)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。


# 小结
#
# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。