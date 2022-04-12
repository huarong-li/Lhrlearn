#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class Game:
    __metaclass__ = ABCMeta
    def __init__(self):
        self._name=''
    
    @abstractmethod
    def initialize(self):
        pass
    @abstractmethod
    def startPlay(self):
        pass
    @abstractmethod
    def endPlay(self):
        pass
    def play(self):
        self.initialize()
        self.startPlay()
        self.endPlay()

class Cricket(Game):
    def initialize(self):
        print("Cricket Game Initialized! Start playing.")
    def startPlay(self):
        print("Cricket Game Start. Enjoy the game!")
    def endPlay(self):
        print("Cricket Game Finished!")

class Football(Game):
    def initialize(self):
        print("Football Game Initialized! Start playing.")
    def startPlay(self):
        print("Football Game Start. Enjoy the game!")
    def endPlay(self):
        print("Football Game Finished!")


if __name__ == '__main__':
    game=Cricket()
    game.play()

    game=Football()
    game.play()

