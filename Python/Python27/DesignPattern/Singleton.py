#!/usr/bin/python
# -*- coding:utf-8 -*-

import random;
import sys;
import platform;
import shutil;

class SingleObject:
    __instance=object()
    @staticmethod
    def getInstance():
        if not isinstance(SingleObject.__instance, SingleObject):
            SingleObject.__instance = SingleObject(SingleObject.__instance)
        return SingleObject.__instance
    
    def __init__(self, key) -> None:
        assert(key == SingleObject.__instance), \
            "SingleObject objects must be created using SingleObject.getInstance"
    def showMessage(self):
        print('Hello world!')

if __name__ == '__main__':
    instance = SingleObject.getInstance()
    instance.showMessage()
    print(dir(instance))

    try:
        instance1=SingleObject(None)
    except AssertionError as e:
        print('An AssertionError flew by ' + str(e))
    finally:
        pass

    try:
        instance2=SingleObject('d')
    except Exception as e:
        print('An exception flew by ' + str(e.args))
    finally:
        pass

    print("end")

