#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Image:
    __metaclass__ = ABCMeta
    @abstractmethod
    def dispaly(self):
        pass

class RealImage(Image):
    def __init__(self, fileName):
        super(RealImage, self).__init__()
        self._fileName = fileName
        self.loadFromDisk(fileName)
    
    def dispaly(self):
        print("Displaying " + self._fileName)
    def loadFromDisk(self, fileName):
        print("Loading " + fileName)

class ProxyImage(Image):
    def __init__(self, fileName):
        super(ProxyImage, self).__init__()
        self._fileName = fileName
        self._realImage = None
    
    def dispaly(self):
        if not self._realImage:
            self._realImage = RealImage(self._fileName)

        print("Displaying " + self._fileName)

if __name__ == '__main__':
    proxyImage = ProxyImage('test_10mb.jpg')
    proxyImage.dispaly()

    proxyImage.dispaly()
