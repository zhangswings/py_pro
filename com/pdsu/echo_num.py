#!/usr/bin/env python
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
# print u'ABC'.encode('uft-8')
# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u'中文'.encode('utf-8')
# 英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同），而中文字符转换后1个Unicode字符将变为3个UTF-8字符，你看到的\xe4就是其中一个字节，因为它的值是228，没有对应的字母可以显示，所以以十六进制显示字节的数值。英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同），而中文字符转换后1个Unicode字符将变为3个UTF-8字符，你看到的\xe4就是其中一个字节，因为它的值是228，没有对应的字母可以显示，所以以十六进制显示字节的数值。
# len()函数可以返回字符串的长度：
print len(u'abc')
# 3
print len('abc')
# 3
print len(u'中文')
# 2
# 反过来，把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法：
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 格式化
# %运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
print 'Hello ,%s'% 'this is my python project.'
print 'Hi %s,This is $%d dollers'%('Tomcat',1000)
# 常见的占位符有：
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print '%2d-%02d' % (2, 1)
print '%.2f'%3.1415926
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print 'Tom is %s years and his last name is %s' %(23,'White')
# 对于Unicode字符串，用法完全一样，但最好确保替换的字符串也是Unicode字符串：
print u'Hi, %s' % u'Michael'
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print 'growth rate: %d%%' % 7
# '\xd6\xd0\xce\xc4'
print u'中文'.encode('gb2312')

