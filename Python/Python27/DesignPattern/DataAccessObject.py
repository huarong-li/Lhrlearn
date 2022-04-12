#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Student:
    def __init__(self, name, rollNo):
        self._rollNo=rollNo
        self._name=name
    def getName(self):
        return self._name
    def setName(self, value):
        self._name=value
    def getRollNo(self):
        return self._rollNo
    def setRollNo(self, value):
        self._rollNo=value

class StudentDao:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._impl=None
    
    @abstractmethod
    def getAllStudents(self):
        pass
    @abstractmethod
    def getStudent(self, rollNo):
        pass
    @abstractmethod
    def updateStudent(self, student):
        pass
    @abstractmethod
    def deleteStudent(self, student):
        pass

class StudentDaoImpl(StudentDao):
    def __init__(self):
        super(StudentDaoImpl, self).__init__()
        self._students=[]
        student1 = Student("Robert",0)
        student2 = Student("John",1)
        self._students.append(student1)
        self._students.append(student2)

    def getAllStudents(self):
        return self._students
    def getStudent(self, rollNo):
        return self._students[rollNo]
    def updateStudent(self, student):
        self._students[student.getRollNo()].setName(student.getName())
        print("Student: Roll No " + str(student.getRollNo()) +", updated in the database")
    def deleteStudent(self, student):
        self._students.remove(student.getRollNo())
        print("Student: Roll No " + str(student.getRollNo()) +", deleted from database")

if __name__ == '__main__':
    studentDao=StudentDaoImpl()

    students=studentDao.getAllStudents()
    for item in students:
        print("Student: [RollNo : " +str(item.getRollNo())+", Name : "+item.getName()+" ]")

    student=studentDao.getAllStudents()[0]
    student.setName("Michael")
    studentDao.updateStudent(student)
 
    student=studentDao.getStudent(0)
    print("Student: [RollNo : "+str(student.getRollNo())+", Name : "+student.getName()+" ]"); 

