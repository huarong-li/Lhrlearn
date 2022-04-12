#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class DependentObject1:
    def __init__(self):
        self._data=""
    def getData(self):
        return self._data
    def setData(self, value):
        self._data=value

class DependentObject2:
    def __init__(self):
        self._data=""
    def getData(self):
        return self._data
    def setData(self, value):
        self._data=value

class CoarseGrainedObject:
    def __init__(self):
        self._data1=DependentObject1()
        self._data2=DependentObject2()
    def getData(self):
        return [self._data1.getData(), self._data2.getData()]
    def setData(self, value1, value2):
        self._data1.setData(value1)
        self._data2.setData(value2)

class CompositeEntity:
    def __init__(self):
        self._cgo=CoarseGrainedObject()
    
    def setData(self, data1, data2):
        self._cgo.setData(data1, data2)
    def getData(self):
        return self._cgo.getData()

class Client:
    def __init__(self):
        self._compositeEntity=CompositeEntity()
    def printData(self):
        data=self._compositeEntity.getData()
        for item in data:
            print("Data: " + item)
    def setData(self, data1, data2):
        self._compositeEntity.setData(data1, data2)

if __name__ == '__main__':
    client = Client()
    client.setData("Test", "Data")
    client.printData()
    client.setData("Second Test", "Data1")
    client.printData()

