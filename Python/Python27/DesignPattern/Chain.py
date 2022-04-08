#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class AbstractLogger:
    __metaclass__ = ABCMeta
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, level):
        self._level = level
        self._nextLogger = None

    def setNextLogger(self, logger):
        self._nextLogger = logger

    def logMessage(self, level, message):
        if self._level <= level:
            self._write(message)
        if self._nextLogger:
            self._nextLogger.logMessage(level, message)
    
    @abstractmethod
    def _write(self, message):
        pass

class ConsoleLogger(AbstractLogger):
    def __init__(self, level):
        super(ConsoleLogger, self).__init__(level)
    
    def _write(self, message):
        print("Standard Console::Logger: " + message)

class ErrorLogger(AbstractLogger):
    def __init__(self, level):
        super(ErrorLogger, self).__init__(level)
    
    def _write(self, message):
        print("Error Console::Logger: " + message)

class FileLogger(AbstractLogger):
    def __init__(self, level):
        super(FileLogger, self).__init__(level)
    
    def _write(self, message):
        print("File::Logger: " + message)

def getChainOfLoggers():
    errorLogger = ErrorLogger(AbstractLogger.ERROR)
    fileLogger = FileLogger(AbstractLogger.INFO)
    consoleLogger = ConsoleLogger(AbstractLogger.DEBUG)

    errorLogger.setNextLogger(fileLogger)
    fileLogger.setNextLogger(consoleLogger)

    return errorLogger


if __name__ == '__main__':
    logger = getChainOfLoggers()

    logger.logMessage(AbstractLogger.INFO, 'This is an information.')
    logger.logMessage(AbstractLogger.DEBUG, 'This is a debug level information.')
    logger.logMessage(AbstractLogger.ERROR, 'This is an error information.')

