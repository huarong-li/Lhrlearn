#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
过滤器模式
过滤器模式（Filter Pattern）或标准模式（Criteria Pattern）是一种设计模式，这种模式允许开发人员使用不同的标准来过滤一组对象，通过逻辑运算以解耦的方式把它们连接起来。这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。
'''

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Person:
    def __init__(self, name, gender, maritalStatus):
        self._name = name
        self._gender = gender
        self._maritalStatus = maritalStatus
    
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender

    @property
    def maritalStatus(self):
        return self._maritalStatus

    def __eq__(self, *args, **kwargs):
        # print('args: %s' % (str(args)))
        # print('kwargs: %s' % str(kwargs))
        other=args[0]
        if not isinstance(other, Person):
            return False
        return (self._name.lower() == other._name.lower()) and (self._gender.lower() == other._gender.lower()) and (self._maritalStatus.lower() == other._maritalStatus.lower())
    def __ne__(self, *args, **kwargs):
        other=args[0]
        if not isinstance(other, Person):
            return True
        return (self._name.lower() != other._name.lower()) or (self._gender.lower() != other._gender.lower()) or (self._maritalStatus.lower() != other._maritalStatus.lower())

class Criteria:
    __metaclass__ = ABCMeta
    def meetCriteria(self, persons):
        pass

class CriteriaMale:
    def __init__(self):
        pass

    def meetCriteria(self, persons):
        male_persons = []
        for person in persons:
            if person.gender.lower() == 'male':
                male_persons.append(person)
        return male_persons

class CriteriaFemale:
    def __init__(self):
        pass

    def meetCriteria(self, persons):
        female_persons = []
        for person in persons:
            if person.gender.lower() == 'female':
                female_persons.append(person)
        return female_persons

class CriteriaSingle:
    def __init__(self):
        pass

    def meetCriteria(self, persons):
        single_persons = []
        for person in persons:
            if person.maritalStatus.lower() == 'single':
                single_persons.append(person)
        return single_persons

class AndCriteria(Criteria):
    def __init__(self, criteria, othercriteria):
        self.criteria = criteria
        self.othercriteria = othercriteria
    def meetCriteria(self, persons):
        first_criteria_persons = self.criteria.meetCriteria(persons)
        return self.othercriteria.meetCriteria(first_criteria_persons)

class OrCriteria(Criteria):
    def __init__(self, criteria, othercriteria):
        self.criteria = criteria
        self.othercriteria = othercriteria
    def meetCriteria(self, persons):
        first_criteria_persons = self.criteria.meetCriteria(persons)
        other_criteria_persons = self.othercriteria.meetCriteria(persons)

        for person in other_criteria_persons:
            try:
                find_idx = first_criteria_persons.index(person)
            except ValueError:
                first_criteria_persons.append(person)
            finally:
                pass

        return first_criteria_persons

def printPersons(persons):
    for person in persons:
        print("Person : [ Name : " + person.name  +", Gender : " + person.gender
            +", Marital Status : " + person.maritalStatus
            +" ]")

if __name__ == '__main__':
    persons = []
 
    persons.append(Person("Robert","Male", "Single"))
    persons.append(Person("John","Male", "Married"))
    persons.append(Person("Laura","Female", "Married"))
    persons.append(Person("Diana","Female", "Single"))
    persons.append(Person("Mike","Male", "Single"))
    persons.append(Person("Bobby","Male", "Single"))

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    singleMale = AndCriteria(single, male)
    singleOrFemale = OrCriteria(single, female)

    print("Males: ")
    printPersons(male.meetCriteria(persons))

    print("Females: ")
    printPersons(female.meetCriteria(persons))

    print("Single Males: ")
    printPersons(singleMale.meetCriteria(persons))

    print("Single Or Females: ")
    printPersons(singleOrFemale.meetCriteria(persons))

    try:
        persons.index(2)
    except ValueError:
        pass
    finally:
        pass
