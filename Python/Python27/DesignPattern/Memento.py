#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Memento:
    def __init__(self, state):
        self._state=state
    def getState(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = ''
    def setState(self, state):
        self._state=state
    def getState(self):
        return self._state
    def saveStateToMemento(self):
        return Memento(self.getState())
    def getStateFromMemento(self, memento):
        self._state=memento.getState()
    
class CareTaker:
    def __init__(self):
        self._mementoList=[]
    def add(self, state):
        self._mementoList.append(state)
    def get(self, index):
        return self._mementoList[index]


if __name__ == '__main__':
    originator = Originator()
    careTaker = CareTaker()
    originator.setState("State #1")
    originator.setState("State #2")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #3")
    careTaker.add(originator.saveStateToMemento())
    originator.setState("State #4")

    print("Current State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(0))
    print("First saved State: " + originator.getState())
    originator.getStateFromMemento(careTaker.get(1))
    print("Second saved State: " + originator.getState())

