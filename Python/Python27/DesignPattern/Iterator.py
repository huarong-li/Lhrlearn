#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Iterator:
    __metaclass__ = ABCMeta
    @abstractmethod
    def hasNext(self):
        return False
    @abstractmethod
    def next(self):
        return None

class NameIterator(Iterator):
    def __init__(self):
        super(NameIterator, self).__init__()
        self._names = ["Robert" , "John" ,"Julie" , "Lora"]
        self._index = 0

    def hasNext(self):
        if self._index < len(self._names):
            return True
        return False
    def next(self):
        if self.hasNext():
            item = self._names[self._index]
            self._index += 1
            return item
        return None

class Container:
    __metaclass__ = ABCMeta
    @abstractmethod
    def getIterator(self):
        return None

class NameRepository(Container):
    def __init__(self):
        super(NameRepository, self).__init__()
        
    def getIterator(self):
        return NameIterator()


if __name__ == '__main__':
    namesRepository = NameRepository()

    iter = namesRepository.getIterator()
    while iter.hasNext():
        name = iter.next()
        print("Name : " + name)

