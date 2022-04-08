#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Employee:
    def __init__(self, name, dept, salary):
        self._name = name
        self._dept = dept
        self._salary = salary
        self.subordinates = []
    @property
    def name(self):
        return self._name
    @property
    def dept(self):
        return self._dept
    @property
    def salary(self):
        return self._salary
    def add(self, item):
        self.subordinates.append(item)
    def remove(self, item):
        try:
            index = self.subordinates.index(item)
            self.subordinates.pop(index)
        except:
            pass
    def __str__(self):
        return "Employee :[ Name : "+ self.name +", dept : "+ self.dept + ", salary :"+ str(self.salary)+" ]"

if __name__ == '__main__':
    CEO = Employee("John","CEO", 30000)
 
    headSales = Employee("Robert","Head Sales", 20000)
 
    headMarketing = Employee("Michel","Head Marketing", 20000)
 
    clerk1 = Employee("Laura","Marketing", 10000)
    clerk2 = Employee("Bob","Marketing", 10000)
 
    salesExecutive1 = Employee("Richard","Sales", 10000)
    salesExecutive2 = Employee("Rob","Sales", 10000)
 
    CEO.add(headSales)
    CEO.add(headMarketing)
 
    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)
 
    headMarketing.add(clerk1)
    headMarketing.add(clerk2)

    print(CEO)
    for headEmployee in CEO.subordinates:
        print(headEmployee)
        for employee in headEmployee.subordinates:
            print(employee)
