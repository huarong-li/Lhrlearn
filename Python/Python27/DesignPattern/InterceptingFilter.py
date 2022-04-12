#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Filter:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    
    @abstractmethod
    def execute(self, request):
        pass

class AuthenticationFilter(Filter):
    def __init__(self):
        super(AuthenticationFilter, self).__init__()
    def execute(self, request):
        print("Authenticating request: " + request)

class DebugFilter(Filter):
    def __init__(self):
        super(DebugFilter, self).__init__()
    def execute(self, request):
        print("request log: " + request)

class Target:
    def __init__(self):
        pass
    def execute(self, request):
        print("Executing request: " + request)

class FilterChain:
    def __init__(self):
        self._filters=[]
        self._target=None
    def addFilter(self, filter):
        self._filters.append(filter)

    def execute(self, requset):
        for item in self._filters:
            item.execute(requset)
        self._target.execute(requset)
    
    def setTarget(self, target):
        self._target=target

class FilterManager:
    def __init__(self, target):
        self._filterChain=FilterChain()
        self._filterChain.setTarget(target)

    def setFilter(self, filter):
        self._filterChain.addFilter(filter)
    def filterRequest(self, requset):
        self._filterChain.execute(requset)
    
class Client:
    def __init__(self):
        self._filterManager=None
    def setFilterManager(self, filterManager):
        self._filterManager=filterManager
    def sendRequest(self, request):
        self._filterManager.filterRequest(request)


if __name__ == '__main__':
    filterManager = FilterManager(Target())
    filterManager.setFilter(AuthenticationFilter())
    filterManager.setFilter(DebugFilter())
 
    client = Client()
    client.setFilterManager(filterManager)
    client.sendRequest("HOME")
