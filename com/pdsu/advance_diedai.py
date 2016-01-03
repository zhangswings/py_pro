#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
在Python中，迭代是通过for ... in来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的，比如Java代码：
'''
for num in range(10):
    print num
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
'''
因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。
由于字符串也是可迭代对象，因此，也可以作用于for循环：
'''
for ch in 'ABC':
    print ch
'''
所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
'''
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3], Iterable) # list是否可迭代
print isinstance(123, Iterable) # 整数是否可迭代
'''
最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
'''
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
'''
上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
'''
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

'''
小结

任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
'''
