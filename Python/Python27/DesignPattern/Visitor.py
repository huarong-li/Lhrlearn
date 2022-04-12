#!/usr/bin/python
# -*- coding:utf-8 -*-

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

