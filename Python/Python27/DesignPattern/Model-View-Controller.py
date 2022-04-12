#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
MVC 模式
MVC 模式代表 Model-View-Controller（模型-视图-控制器） 模式。这种模式用于应用程序的分层开发。

Model（模型） - 模型代表一个存取数据的对象或 JAVA POJO。它也可以带有逻辑，在数据变化时更新控制器。
View（视图） - 视图代表模型包含的数据的可视化。
Controller（控制器） - 控制器作用于模型和视图上。它控制数据流向模型对象，并在数据变化时更新视图。它使视图与模型分离开
'''

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Student:
    def __init__(self):
        self._rollNo=""
        self._name=""
    def getName(self):
        return self._name
    def setName(self, value):
        self._name=value
    def getRollNo(self):
        return self._rollNo
    def setRollNo(self, value):
        self._rollNo=value

class StudentView:
    def __init__(self):
        pass
    def printStudentDetails(self, name, rollNo):
        print("Student: ")
        print("Name: " + name)
        print("RollNo: " + rollNo)

class StudentController:
    def __init__(self, model, view):
        self._model=model
        self._view=view
    def getStudentName(self):
        return self._model.getName()
    def setStudentName(self, name):
        self._model.setName(name)
    def getStudentRollNo(self):
        return self._model.getRollNo()
    def setStudentRollNo(self, rollNo):
        self._model.setRollNo(rollNo)
    def updateView(self):
        self._view.printStudentDetails(self.getStudentName(), self.getStudentRollNo())

def retrieveStudentFromDatabase():
    student = Student()
    student.setName("Robert")
    student.setRollNo("10")
    return student


if __name__ == '__main__':
    model=retrieveStudentFromDatabase()

    view=StudentView()

    controller=StudentController(model, view)
    controller.updateView()

    controller.setStudentName("John")
    controller.updateView()

