#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

from abc import ABCMeta
from abc import abstractmethod

class HomeView:
    def show(self):
        print("Displaying Home Page")

class StudentView:
    def show(self):
        print("Displaying Student Page")

class Dispatcher:
    def __init__(self):
        self._studentView=StudentView()
        self._homeView=HomeView()
    def dispatch(self, request):
        if request == "STUDENT":
            self._studentView.show()
        else:
            self._homeView.show()
    
class FrontController:
    def __init__(self):
        self._dispatcher=Dispatcher()
    def __isAuthenticUser(self):
        print("User is authenticated successfully.")
        return True
    def trackRequest(self, request):
        print("Page requested: " + request)
    def dispatchRequest(self, request):
        self.trackRequest(request)
        if self.__isAuthenticUser():
            self._dispatcher.dispatch(request)

if __name__ == '__main__':
    frontController = FrontController()
    frontController.dispatchRequest("HOME")
    frontController.dispatchRequest("STUDENT")

