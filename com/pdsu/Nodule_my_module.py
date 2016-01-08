#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from PIL import Image
im=Image.open("a.jpg")
im.show()
'''
注意：第一行的Image是模块名；第二行的img是一个Image对象； Image类是在Image模块中定义的。关于Image模块和Image类，切记不要混淆了。
现在，我们就可以对img进行各种操作了，所有对img的 操作最终都会反映到到dip.img图像上。
'''
# PIL提供了丰富的功能模块：Image,ImageDraw,ImageEnhance,ImageFile等等。
# 最常用到的模块是 Image,ImageDraw,ImageEnhance这三个模块。
# 调整图像大小:
new_img=im.resize((128,128),Image.BILINEAR)
new_img.save("new_img.jpg")