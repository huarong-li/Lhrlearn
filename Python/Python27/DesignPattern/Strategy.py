#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Strategy:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._name=''
    
    @abstractmethod
    def doOperation(self, num1, num2):
        pass

class OperationAdd(Strategy):
    def __init__(self):
        super(OperationAdd, self).__init__()
    def doOperation(self, num1, num2):
        return num1+num2

class OperationSubstract(Strategy):
    def __init__(self):
        super(OperationSubstract, self).__init__()
    def doOperation(self, num1, num2):
        return num1-num2

class OperationMultiply(Strategy):
    def __init__(self):
        super(OperationMultiply, self).__init__()
    def doOperation(self, num1, num2):
        return num1*num2

class Context:
    def __init__(self, strategy):
        self._strategy=strategy
    def executeStrategy(self, num1, num2):
        return self._strategy.doOperation(num1, num2)

if __name__ == '__main__':
    context = Context(OperationAdd())
    print("10 + 5 = " + str(context.executeStrategy(10, 5)))

    context = Context(OperationSubstract())
    print("10 - 5 = " + str(context.executeStrategy(10, 5)))

    context = Context(OperationMultiply())
    print("10 * 5 = " + str(context.executeStrategy(10, 5)))
