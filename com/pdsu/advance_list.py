#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
列表生成式
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：
'''
print range(1,11)
'''
但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？L.append(x * x)方法一是循环：
'''
L = []
for x in range(1, 11):
     L.append(x * x)
print L
'''
但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
'''
print [x * x for x in range(1, 11)]
'''
还可以使用两层循环，可以生成全排列：
'''
print [m + n for m in 'ABC' for n in 'XYZ']
'''
三层和三层以上的循环就很少用到了。
运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
'''
# 导入os模块，模块的概念后面讲到
import os
print [d for d in os.listdir('.')]
# os.listdir可以列出文件和目录
# ['advance_diedai.py', 'advance_feature.py', 'advance_list.py', 'advance_qiepian.py', 'dict_py.py', 'echo_num.py', 'Echo_str.py', 'function_args.py', 'function_help.py', 'function_recursion.py', 'if_else.py', 'list_tuple.py', 'set_py.py', 'tuple_list', '__init__.py']
'''
for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k, '=', v
'''
因此，列表生成式也可以使用两个变量来生成list：
'''
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + ' = ' + v for k, v in d.iteritems()]
'''
最后把一个list中所有的字符串变成小写：
'''
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]
'''
最后把一个list中所有的字符串变成大写：
'''
print [s.upper() for s in L]
'''
小结

运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
'''

# 思考：如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# AttributeError: 'int' object has no attribute 'lower'
L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() for s in L]
'''
使用内建的isinstance函数可以判断一个变量是不是字符串：

>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
请修改列表生成式，通过添加if语句保证列表生成式能正确地执行。
'''
print  [s.lower() if isinstance(s,str) else s for s in L]




# 讨论
'''
从楼上lber19535提供的链接来看，如果要一定要区分两个表达式的类型的话，我有不同的意见。

列表生成器

comprehension ::=  expression comp_for
comp_for      ::=  "for" target_list "in" or_test [comp_iter]
comp_iter     ::=  comp_for | comp_if
comp_if       ::=  "if" expression_nocond [comp_iter]
条件表达式

conditional_expression ::=  or_test ["if" or_test "else" expression]
expression             ::=  conditional_expression | lambda_expr
expression_nocond      ::=  or_test | lambda_expr_nocond
看来条件表达式没有for。

条件表达式 | lambda表达式 + for 是列表生成器的一种形式。

L= [s.lower() if isinstance(s,str) else s for s in L]
其中s.lower() if isinstance(s,str) else s是条件表达式，这是列表生成器。

而另一个

L= [s.lower() for s in L if isinstance(s,str) else s for s in L]
其中s.lower() for s in L if isinstance(s,str) else s不是条件表达式，if isinstance(s,str) else s for s in L也不是条件表达式，而符合列表生成器的comp_if ::= "if" expression_nocond [comp_iter]。所以这也是列表生成器。
'''