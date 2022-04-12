#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
访问者模式
在访问者模式（Visitor Pattern）中，我们使用了一个访问者类，它改变了元素类的执行算法。通过这种方式，元素的执行算法可以随着访问者改变而改变。这种类型的设计模式属于行为型模式。根据模式，元素对象已接受访问者对象，这样访问者对象就可以处理元素对象上的操作。
'''

'''
介绍
意图：主要将数据结构与数据操作分离。

主要解决：稳定的数据结构和易变的操作耦合问题。

何时使用：需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作"污染"这些对象的类，使用访问者模式将这些封装到类中。

如何解决：在被访问的类里面加一个对外提供接待访问者的接口。

关键代码：在数据基础类里面有一个方法接受访问者，将自身引用传入访问者。

应用实例：您在朋友家做客，您是访问者，朋友接受您的访问，您通过朋友的描述，然后对朋友的描述做出一个判断，这就是访问者模式。

优点： 1、符合单一职责原则。 2、优秀的扩展性。 3、灵活性。

缺点： 1、具体元素对访问者公布细节，违反了迪米特原则。 2、具体元素变更比较困难。 3、违反了依赖倒置原则，依赖了具体类，没有依赖抽象。

使用场景： 1、对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。 2、需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作"污染"这些对象的类，也不希望在增加新操作时修改这些类。

注意事项：访问者可以对功能进行统一，可以做报表、UI、拦截器与过滤器。
'''

import random;
import sys;
import platform;
import shutil;
import functools

from abc import ABCMeta
from abc import abstractmethod

class ComputerPart:
    __metaclass__=ABCMeta
    @abstractmethod
    def accept(self, computerPartVisitor):
        pass

class Keyboard(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)

class Monitor(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)

class Mouse(ComputerPart):
    def accept(self, computerPartVisitor):
        computerPartVisitor.visit(self)

class Computer(ComputerPart):
    def __init__(self):
        self._parts=[Mouse(), Keyboard(), Monitor()]

    def accept(self, computerPartVisitor):
        for item in self._parts:
            item.accept(computerPartVisitor)
        computerPartVisitor.visit(self)

class ComputerPartVisitorStract:
    __metaclass__=ABCMeta

    @abstractmethod
    def visit(self, args):
        pass

class ComputerPartVisitor(ComputerPartVisitorStract):
    def __init__(self):
        super(ComputerPartVisitor, self).__init__()
    # 3.8版本后支持singledispatchmethod，对类函数生效, singledispatch只对函数生效
    # @functools.singledispatch
    def visit(self, args):
        # super(ComputerPartVisitor, self).visit(args)
        if isinstance(args, Keyboard):
            print("Displaying Keyboard.")
        if isinstance(args, Monitor):
            print("Displaying Monitor.")
        if isinstance(args, Mouse):
            print("Displaying Mouse.")
        if isinstance(args, Computer):
            print("Displaying Computer.")
        
    # @visit.register(Keyboard)
    # def _(args):
    #     print("Displaying Keyboard.")
    # @visit.register(Monitor)
    # def _(args):
    #     print("Displaying Monitor.")
    # @visit.register(Mouse)
    # def _(args):
    #     print("Displaying Mouse.")
    # @visit.register(Computer)
    # def _(args):
    #     print("Displaying Computer.")

if __name__ == '__main__':
    computer = Computer()
    computer.accept(ComputerPartVisitor())

