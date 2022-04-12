#!/usr/bin/python
# -*- coding:utf-8 -*-

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

