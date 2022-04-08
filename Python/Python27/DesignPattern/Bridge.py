#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class DrawAPI():
    __metaclass__ = ABCMeta
    @abstractmethod
    def drawCircle(self, radius, x, y):
        pass

class RedCircle(DrawAPI):
    def drawCircle(self, radius, x, y):
        print("Drawing Circle[ color: red, radius: " + str(radius) +", x: " +str(x)+", y: "+ str(y) +" ]")

class GreenCircle(DrawAPI):
    def __init__(self):
        pass
    def drawCircle(self, radius, x, y):
        print("Drawing Circle[ color: green, radius: " + str(radius) +", x: " +str(x)+", y: "+ str(y) +" ]")

class Shape:
    def __init__(self, drawAPI):
        self._drawAPI = drawAPI
    @property
    def drawAPI(self):
        return self._drawAPI
    
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, x, y, radius, drawAPI):
        self._x = x
        self._y = y
        self._radius = radius
        self.drawAPI = drawAPI
    
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def radius(self):
        return self._radius

    def draw(self):
        self.drawAPI.drawCircle(self.radius, self.x, self.y)


if __name__ == '__main__':
    shape1 = Circle(100, 100, 10, RedCircle())
    shape2 = Circle(100, 100, 10, GreenCircle())

    shape1.draw()
    shape2.draw()
