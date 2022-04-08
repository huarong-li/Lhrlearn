#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

class Shape(object):
    def __init__(self):
        self._id = ''
        self._type = 'Shape'
    @property
    def id(self):
        return self._id
    @property
    def type(self):
        return self._type
    def getType(self):
        return self._type
    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id
    def clone(self):
        clone_obj = None
        try:
            clone_obj = Shape()
        except Exception as e:
            print(e.args)
        else:
            pass
        finally:
            return clone_obj
    def draw(self):
        print("Inside Shape::draw() method.")

class Circle(Shape):
    def __init__(self):
        self._id = ''
        self._type = 'Circle'
    def draw(self):
        print("Inside Circle::draw() method.")
    def clone(self):
        clone_new = Circle()
        clone_new._type = self._type
        clone_new._id = self._id
        return clone_new

class Rectangle(Shape):
    def __init__(self):
        self._id = ''
        self._type = 'Rectangle'
    def draw(self):
        super(Rectangle, self).draw()
        print("Inside Rectangle::draw() method.")
    def clone(self):
        clone_new = Rectangle()
        clone_new._type = self._type
        clone_new._id = self._id
        return clone_new

class Square(Shape):
    def __init__(self):
        self._id = ''
        self._type = 'Square'
    # def draw(self):
    #     print("Inside Square::draw() method.")
    def clone(self):
        clone_new = Square()
        clone_new._type = self._type
        clone_new._id = self._id
        return clone_new

class ShapeCache:
    __shapeMap={}
    @staticmethod
    def getShape(id):
        if id in ShapeCache.__shapeMap.keys():
            return ShapeCache.__shapeMap[id].clone()
        
    @staticmethod
    def loadCache():
        circle = Circle()
        circle.setId('1')
        ShapeCache.__shapeMap[circle.getId()] = circle

        rectangle = Rectangle()
        rectangle.setId('2')
        ShapeCache.__shapeMap[rectangle.getId()] = rectangle

        square = Square()
        square.setId('3')
        ShapeCache.__shapeMap[square.getId()] = square

if __name__ == '__main__':
    ShapeCache.loadCache()

    shape1 = ShapeCache.getShape('1')
    print('Shape: ' + shape1.getType())
    shape1.draw()

    shape2 = ShapeCache.getShape('2')
    print('Shape: ' + shape2.getType())
    shape2.draw()

    shape3 = ShapeCache.getShape('3')
    print('Shape: ' + shape3.getType())
    shape3.draw()

