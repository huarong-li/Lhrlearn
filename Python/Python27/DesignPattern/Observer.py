#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Subject:
    def __init__(self):
        self._observers=[]
        self._state=0
    def getState(self):
        return self._state
    def setState(self, state):
        self._state=state
        self.notifyAllObservers()
    def attach(self, observer):
        self._observers.append(observer)
    def notifyAllObservers(self):
        for item in self._observers:
            item.update()

class Observer:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._subject=None
    @property
    def Subject(self):
        return self._subject
    @Subject.setter
    def Subject(self, value):
        self._subject=value

    @abstractmethod
    def update(self):
        pass

class BinaryObserver(Observer):
    def __init__(self, subject):
        super(BinaryObserver, self).__init__()
        self.Subject=subject
        self.Subject.attach(self)
    def update(self):
        print("Binary String: " + str(bin(self.Subject.getState())))

class OctalObserver(Observer):
    def __init__(self, subject):
        super(OctalObserver, self).__init__()
        self.Subject=subject
        self.Subject.attach(self)
    def update(self):
        print("Octal String: " + str(oct(self.Subject.getState())))

class HexaObserver(Observer):
    def __init__(self, subject):
        super(HexaObserver, self).__init__()
        self.Subject=subject
        self.Subject.attach(self)
    def update(self):
        print("Hex String: " + str(hex(self.Subject.getState())))

if __name__ == '__main__':
    subject=Subject()

    hexOb=HexaObserver(subject)
    octOb=OctalObserver(subject)
    binOb=BinaryObserver(subject)

    print("First state change: 15")
    subject.setState(15)
    print("First state change: 10")
    subject.setState(10)
