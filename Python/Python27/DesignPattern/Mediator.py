#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;
import datetime

from abc import ABCMeta
from abc import abstractmethod

class ChatRoom:
    @staticmethod
    def sendMessage(user, message):
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " [" + user.getName() +"] : " + message)

class User:
    def __init__(self, name):
        self._name=name
    def getName(self):
        return self._name
    def setName(self, name):
        self._name=name
    def sendMessage(self, message):
        ChatRoom.sendMessage(self, message)  

if __name__ == '__main__':
    robert = User("Robert")
    john = User("John")
 
    robert.sendMessage("Hi! John!")
    john.sendMessage("Hello! Robert!")

