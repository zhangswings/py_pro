#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# 解释一下类属性和实例属性。直接在class中定义的是类属性：
class Student(object):
    name = 'Student'

# 实例属性必须通过实例来绑定，比如self.name = 'xxx'。来测试一下：
'''
>>> # 创建实例s：
>>> s = Student()
>>> # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性：
>>> print(s.name)
Student
>>> # 这和调用Student.name是一样的：
>>> print(Student.name)
Student
>>> # 给实例绑定name属性：
>>> s.name = 'Michael'
>>> # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性：
>>> print(s.name)
Michael
>>> # 但是类属性并未消失，用Student.name仍然可以访问：
>>> print(Student.name)
Student
>>> # 如果删除实例的name属性：
>>> del s.name
>>> # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了：
>>> print(s.name)
Student
'''
# 因此，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字。

# 在我们编写的ORM中，ModelMetaclass会删除掉User类的所有类属性，目的就是避免造成混淆。