#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Shape:
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Shape: Circle")
    
class Rectangle(Shape):
    def draw(self):
        print("Shape: Rectangle")
    
class ShapeDecorator:
    def __init__(self, shape):
        self._shape = shape
        
    @property
    def shape(self):
        return self._shape
    def draw(self):
        self._shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def __init__(self, shape):
        self._shape = shape

    def draw(self):
        self._shape.draw()
        self.setRedBorder(self._shape)

    def setRedBorder(self, decoratedShape):
        print("Border Color: Red")

if __name__ == '__main__':
    circle = Circle()
    redCircle = RedShapeDecorator(Circle())
    redRectangle = RedShapeDecorator(Rectangle())

    print("Circle with normal border")
    circle.draw()

    print("Circle of red border")
    redCircle.draw()

    print("Rectangl of red border")
    redRectangle.draw()
