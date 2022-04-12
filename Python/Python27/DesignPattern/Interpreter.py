#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

'''解释器模式（Interpreter Pattern）提供了评估语言的语法或表达式的方式，它属于行为型模式。
这种模式实现了一个表达式接口，该接口解释一个特定的上下文。
这种模式被用在 SQL 解析、符号处理引擎等。'''

class Expression:
    __metaclass__ = ABCMeta
    @abstractmethod
    def interpret(self, context):
        return False

class TerminalExpression(Exception):
    def __init__(self, data):
        super(TerminalExpression, self).__init__()
        self._data = data
    
    def interpret(self, context):
        if self._data in context:
            return True
        return False

class OrExpression(Expression):
    def __init__(self, expr1, expr2):
        super(OrExpression, self).__init__()
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) or self._expr2.interpret(context)

class AndExpression(Expression):
    def __init__(self, expr1, expr2):
        super(AndExpression, self).__init__()
        self._expr1 = expr1
        self._expr2 = expr2

    def interpret(self, context):
        return self._expr1.interpret(context) and self._expr2.interpret(context)    

def getMaleExpression():
    robert = TerminalExpression("Robert")
    john = TerminalExpression("John")
    return OrExpression(robert, john)

def getMarriedWomanExpression():
    julie = TerminalExpression("Julie")
    married = TerminalExpression("Married")
    return AndExpression(julie, married)


if __name__ == '__main__':
    isMale = getMaleExpression()
    isMarriedWoman = getMarriedWomanExpression()
 
    print("John is male? " + str(isMale.interpret("John")))
    print("Julie is a married women? " + str(isMarriedWoman.interpret("Married Julie")))

