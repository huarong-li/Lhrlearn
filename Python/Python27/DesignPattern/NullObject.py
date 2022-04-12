#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class AbstractCustomer:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._name=''
    
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, value):
        self._name=value
    @abstractmethod
    def isNil(self):
        pass
    @abstractmethod
    def getName(self):
        pass

class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        super(RealCustomer, self).__init__()
        self.Name=name
    def isNil(self):
        return False
    def getName(self):
        return self.Name

class NullCustomer(AbstractCustomer):
    def __init__(self):
        super(NullCustomer, self).__init__()

    def isNil(self):
        return True
    def getName(self):
        return "Not Available in Customer Database"

class CustomerFactory:
    Names=["Rob", "Joe", "Julie"]
    @staticmethod
    def getCustomer(name):
        for item in CustomerFactory.Names:
            if item == name:
                return RealCustomer(name)
        return NullCustomer()


if __name__ == '__main__':
    customer1=CustomerFactory.getCustomer("Rob")
    customer2=CustomerFactory.getCustomer("Bob")
    customer3=CustomerFactory.getCustomer("Julie")
    customer4=CustomerFactory.getCustomer("Laura")

    print("Customers")
    print(customer1.getName())
    print(customer2.getName())
    print(customer3.getName())
    print(customer4.getName())

