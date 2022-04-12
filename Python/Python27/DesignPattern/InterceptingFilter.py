#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
拦截过滤器模式
拦截过滤器模式（Intercepting Filter Pattern）用于对应用程序的请求或响应做一些预处理/后处理。定义过滤器，并在把请求传给实际目标应用程序之前应用在请求上。过滤器可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。以下是这种设计模式的实体。

过滤器（Filter） - 过滤器在请求处理程序执行请求之前或之后，执行某些任务。
过滤器链（Filter Chain） - 过滤器链带有多个过滤器，并在 Target 上按照定义的顺序执行这些过滤器。
Target - Target 对象是请求处理程序。
过滤管理器（Filter Manager） - 过滤管理器管理过滤器和过滤器链。
客户端（Client） - Client 是向 Target 对象发送请求的对象。
'''

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
