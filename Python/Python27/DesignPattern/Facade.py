#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Shape():
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self):
        super(Circle, self).__init__()
    
    def draw(self):
        print("Circle::draw()")

class Square(Shape):
    def __init__(self):
        super(Square, self).__init__()
    
    def draw(self):
        print("Square::draw()")

class Rectangle(Shape):
    def __init__(self):
        super(Rectangle, self).__init__()
    
    def draw(self):
        print("Rectangle::draw()")

class ShapeMarker:
    def __init__(self):
        self._circle = Circle()
        self._rectangle = Rectangle()
        self._square = Square()

    def drawCirle(self):
        self._circle.draw()
    def drawRectangle(self):
        self._rectangle.draw()
    def drawSquare(self):
        self._square.draw()

if __name__ == '__main__':
    shapemarker = ShapeMarker()

    shapemarker.drawCirle()
    shapemarker.drawRectangle()
    shapemarker.drawSquare()

