#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image
im=Image.open("a.jpg")
# im.show()
'''
注意：第一行的Image是模块名；第二行的img是一个Image对象； Image类是在Image模块中定义的。关于Image模块和Image类，切记不要混淆了。
现在，我们就可以对img进行各种操作了，所有对img的 操作最终都会反映到到dip.img图像上。
'''
# PIL提供了丰富的功能模块：Image,ImageDraw,ImageEnhance,ImageFile等等。
# 最常用到的模块是 Image,ImageDraw,ImageEnhance这三个模块。
# 调整图像大小:
new_img=im.resize((128,128),Image.BILINEAR)
new_img.save("new_img.jpg")
# 原来的图像大小是256x256,现在，保存的new_img.jpg的大小是128x128。
# 就是这么简单，需要说明的是Image.BILINEAR指定采用双线性法对像素点插值。
#旋转图像：
# 现在我们把刚才调整过大小的图像旋转45度：
rot_img=im.rotate(45)
rot_img.show()
'''
总结：
在批处理或者简单的Python图像处理任务中，采用Python和PIL（Python Image Library）的组合来完成图像处理任务是一个很不错的选择。
设想有一个需要对某个文件夹下的所有图像将对比度提高2倍的任务。
用Python来做将是 十分简单的。当然，我也不得不承认Python在图像处理方面的功能还比较弱，显然还不适合用来进行滤波、特征提取等等一些更为复杂的应用。
我个人的观点 是，当你要实现这些“高级”的算法的时候，好吧，把它交给MATLAB去完成。
但是，如果你面对的只是一个通常的不要求很复杂算法的图像处理任务，那 么，Python应该才是你的最佳搭档。
'''
