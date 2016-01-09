#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
'''
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print 'Animal is running'
# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass
class Cat(Animal):
    pass
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。

# 继承有什么好处？最大的好处是子类获得了父类的全部功能。
# 由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog = Dog()
dog.run()

cat = Cat()
cat.run()

# 当然，也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'
        pass

dog = Dog()
dog.run()
dog.eat()
# 继承的第二个好处需要我们对代码做一点改进。
# 你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。

# 要理解什么是多态，我们首先要对数据类型再作一点说明。
# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断：
print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
# 看来a、b、c确实对应着list、Animal、Dog这3种类型。
# 但是等等，试试：
print isinstance(c,Animal)#True
print isinstance(b,Dog)#False
# 看来c不仅仅是Dog，c还是Animal！
# Dog可以看成Animal，但Animal不可以看成Dog。

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()
# 当我们传入Animal的实例时，run_twice()就打印出：
run_twice(Animal())

# 当我们传入Dog的实例时，run_twice()就打印出：
run_twice(Dog())
# 当我们传入Cat的实例时，run_twice()就打印出：

# >>> run_twice(Cat())
# Cat is running...
# Cat is running...

# 看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'

# 当我们调用run_twice()时，传入Tortoise的实例：
run_twice(Tortoise())