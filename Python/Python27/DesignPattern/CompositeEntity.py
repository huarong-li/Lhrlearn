#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
组合实体模式
组合实体模式（Composite Entity Pattern）用在 EJB 持久化机制中。一个组合实体是一个 EJB 实体 bean，代表了对象的图解。当更新一个组合实体时，内部依赖对象 beans 会自动更新，因为它们是由 EJB 实体 bean 管理的。以下是组合实体 bean 的参与者。

组合实体（Composite Entity） - 它是主要的实体 bean。它可以是粗粒的，或者可以包含一个粗粒度对象，用于持续生命周期。
粗粒度对象（Coarse-Grained Object） - 该对象包含依赖对象。它有自己的生命周期，也能管理依赖对象的生命周期。
依赖对象（Dependent Object） - 依赖对象是一个持续生命周期依赖于粗粒度对象的对象。
策略（Strategies） - 策略表示如何实现组合实体。
'''

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

