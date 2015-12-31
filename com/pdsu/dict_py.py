#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# 使用dict和set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
# 用Python写一个dict如下：
print d['Bob']
# 为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。
# 假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
# 第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字，无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
# 这种key-value存储方式
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
# d['Jack']=90
d['Jack']=101
print d['Jack']
# 101
# 如果key不存在，dict就会报错
flag='Thoms' in d
print flag
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print d.get('Thoms')
# None 注意：返回None的时候Python的交互式命令行不显示结果。
print d.get('Thoms',-1)
# -1
# 删除一个 key pop( )
d.pop("Bob")
print d
# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
# >>> key = [1, 2, 3]
# >>> d[key] = 'a list'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'






