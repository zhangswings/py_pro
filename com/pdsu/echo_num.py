#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# name=raw_input('Please input your Name: ')
name="Simple Name"
print 'Hello,',name
items=[1,2,4,5,7,8]
# head=1
# head, *tail=items
# print tail
# 16进制
print 0x12
# 'A' 65
print ord('A')
# 56 'A'
print chr(65)
# 输出中文
print u'中文'
# 写u'中'和u'\u4e2d'是一样的，\u后面是十六进制的Unicode码。因此，u'A'和u'\u0041'也是一样的。
print u'\u4e2d'
# 两种字符串如何相互转换？字符串'xxx'虽然是ASCII编码，但也可以看成是UTF-8编码，而u'xxx'则只能是Unicode编码。
# print (u'ABC'.encode('uft-8'))
# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u'中文'.encode('utf-8')

