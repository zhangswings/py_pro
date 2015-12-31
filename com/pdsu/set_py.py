#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
print s
# 注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。
# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print s
# 添加 add(key)
s.add(9)
print s
# remove(key)方法可以删除元素
s.remove(1)
print s
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# 两个set的交集
print s1&s2
# 两个set的并集
print s1|s2
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
# 试试把list放入set，看看是否会报错。


# 再议不可变对象
# 上面我们讲了，str是不变对象，而list是可变对象。

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c', 'b', 'a']
print a
# 而对于不可变对象，比如str，对str进行操作呢：
aa='abc'
print aa
aa_r=aa.replace('a','A')
print 'aa = ',aa
print 'aa_r = ',aa_r

# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最常用的key是字符串。

# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
