#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
而处理学生成绩可以通过函数实现，比如打印学生的成绩：

def print_score(std):
    print '%s: %s' % (std['name'], std['score'])
如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，
首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
'''
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
def print_score(std):
    print '%s: %s' % (std['name'], std['score'])
print_score(std1)
print_score(std2)
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_scpre(self):
        print '%s: %s'%(self.name,self.score)

bart=Student('Bart Simpson',67)
zhang=Student('zhang',100)
bart.print_scpre()
zhang.print_scpre()
# 面向对象编程，封装、继承、多态

