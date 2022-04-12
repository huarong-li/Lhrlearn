#!/usr/bin/python
# -*- coding:utf-8 -*-

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

