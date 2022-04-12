#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
业务代表模式
业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。在业务层中我们有以下实体。

客户端（Client） - 表示层代码可以是 JSP、servlet 或 UI java 代码。
业务代表（Business Delegate） - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
查询服务（LookUp Service） - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
业务服务（Business Service） - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。
'''

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class BusinessService:
    __metaclass__=ABCMeta
    @abstractmethod
    def doProcessing(self):
        pass

class EJBService(BusinessService):
    def doProcessing(self):
        print("Processing task by invoking EJB Service")

class JMSService(BusinessService):
    def doProcessing(self):
        print("Processing task by invoking JMS Service")

class BusinessLookUp:
    def __init__(self):
        pass
    def getBusinessService(self, serviceType):
        if serviceType == "EJB":
            return EJBService()
        else:
            return JMSService()

class BusinessDelegate:
    def __init__(self):
        self._lookupService=BusinessLookUp()
        self._businessService=None
        self._serviceType=""
    def setServiceType(self, serviceType):
        self._serviceType=serviceType
    def doTask(self):
        businessServce=self._lookupService.getBusinessService(self._serviceType)
        businessServce.doProcessing()

class Client:
    def __init__(self, businessService):
        self._businessService=businessService
    def doTask(self):
        self._businessService.doTask()

if __name__ == '__main__':
    businessDelegate = BusinessDelegate()
    businessDelegate.setServiceType("EJB")
 
    client = Client(businessDelegate)
    client.doTask()
 
    businessDelegate.setServiceType("JMS")
    client.doTask()

