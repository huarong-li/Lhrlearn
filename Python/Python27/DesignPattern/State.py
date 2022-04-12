#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class State:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass
    @abstractmethod
    def doAction(self, value):
        pass

class StartState(State):
    def __init__(self):
        super(StartState, self).__init__()
    def doAction(self, context):
        print("Player is in start state")
        context.setState(self)
    def __str__(self):
        return "Start state"

class StopState(State):
    def __init__(self):
        super(StopState, self).__init__()
    def doAction(self, context):
        print("Player is in stop state")
        context.setState(self)
    def __str__(self):
        return "Stop state"

class Context:
    def __init__(self):
        self._state=None
    def getState(self):
        return self._state
    def setState(self, state):
        self._state=state

if __name__ == '__main__':
    context=Context()

    stateState=StartState()
    stateState.doAction(context)

    print(context.getState())

    stopState=StopState()
    stopState.doAction(context)

    print(context.getState())
