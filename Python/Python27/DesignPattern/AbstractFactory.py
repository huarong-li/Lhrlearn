#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self):
        print("Draw Circle")

class Square(Shape):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self):
        print("Draw Square")

class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()
    
    def draw(self):
        print("Draw Rectangle")

class ShapeFactory:
    def getShape(self, type):
        if type == None:
            return None
        elif type == 'Circle':
            return Circle()
        elif type == 'Square':
            return Square()
        elif type == 'Rectangle':
            return Rectangle()

if __name__ == '__main__':
    shapefactory=ShapeFactory()
    shape1 = shapefactory.getShape('Circle')
    shape1.draw()

    shape1 = shapefactory.getShape('Square')
    shape1.draw()

    shape1 = shapefactory.getShape('Rectangle')
    shape1.draw()
