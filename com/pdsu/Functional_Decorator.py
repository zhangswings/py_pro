#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
装饰器
'''
'''
装饰器

阅读: 38795
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

>>> def now():
...     print '2013-12-25'
...
>>> f = now
>>> f()
2013-12-25
函数对象有一个__name__属性，可以拿到函数的名字：

>>> now.__name__
'now'
>>> f.__name__
'now'
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

@log
def now():
    print '2013-12-25'
调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

>>> now()
call now():
2013-12-25
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
这个3层嵌套的decorator用法如下：

@log('execute')
def now():
    print '2013-12-25'
执行结果如下：

>>> now()
execute now():
2013-12-25
和两层嵌套的decorator相比，3层嵌套的效果是这样的：

>>> now = log('execute')(now)
我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

>>> now.__name__
'wrapper'
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。

小结

在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''
def now():
    print '2016-01-01'
f = now()
f
print now.__name__
# print f.__name__
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2016-01-01'
now()

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2013-12-25'

now()

'''
小结

在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
'''

'''
装饰器的作用
可以极大的简化代码，避免每个函数编写重复性的代码
1.打印日志：@log
2.检测性能：@performance
3.数据库事务：@transaction
4.URL路由：@post('/register')
'''
'''
任务
请编写一个@performance，它可以打印出函数调用的时间。
'''
import time

def performance(f):
    def print_time(*args, **kw):
        print 'call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return f(*args,**kw)
    return print_time

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)


'''
编写无参数decorator
Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。

使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。

考察一个@log的定义：

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
对于阶乘函数，@log工作得很好：

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
结果：

call factorial()...
3628800
但是，对于参数不是一个的函数，调用将报错：

@log
def add(x, y):
    return x + y
print add(1, 2)
结果：

Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print add(1,2)
TypeError: fn() takes exactly 1 argument (2 given)
因为 add() 函数需要传入两个参数，但是 @log 写死了只含一个参数的返回函数。

要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：

def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
现在，对于任意函数，@log 都能正常工作。
'''

