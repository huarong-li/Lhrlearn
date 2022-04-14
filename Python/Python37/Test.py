#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import tkinter
import Tkinter.TkTestClass
import math
import configparser

class MyTestClass(object):
    @staticmethod
    def TestOutput(parameter_list):
        print('staticmethod-MyTestClass: ', parameter_list)
    @classmethod
    def TestClassMethod(cls):
        print('MyTestClass-ClassMethod: ', cls)
    
    def TestMethod(self):
        print('MyTestClass-Comm: ', vars(self))

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

def helloCallBack():
    print("你好 python!")
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    text = json.loads(jsonData)
    print(text)

    print(chr(64))
    print(ord('r'))
    print(hex(3423445))
    print(oct(3423445))

    a = 60 #0011 1100
    b = 13 #0000 1101
    c = 60

    print(bin(a))
    print(bin(b))
    print(id(c))

    print(bin(a&b)) #= 0000 1100
    print(bin(a|b)) #= 0011 1101
    print(bin(a^b)) #= 0011 0001
    print(bin(~a))  #= 1100 0011

    seq = ['one', 'two', 'three']
    for i, element in enumerate(seq):
        print(i, element)
    
    newlist = filter(is_sqr, range(1, 101))   
    print(tuple(newlist))
    print(list(newlist))

    myCls = MyTestClass()
    print(type(1), type(myCls))
    print(MyTestClass.__name__)
    print(vars(MyTestClass))

def unicodeTest():
    beg = int(input("请输入起始值："))
    end = int(input("请输入终止值："))
    print("十进制编码\t十六进制编码\t字符")
    for i in range(beg,end+1):
        print("{}\t\t\t{}\t\t\t{}".format(i,hex(i),chr(i)))

def buildFunTest():
    print('{:08b}'.format(11))
    MyTestClass.TestClassMethod()

    test = MyTestClass()
    test.TestMethod()

    config1 = configparser.ConfigParser()
    #bIsPy = config1.getint("Py", "", 1)

    print(globals())

if __name__ == "__main__":
    MyTestClass.TestOutput(45)
    helloCallBack()
    #unicodeTest()

    buildFunTest()

    tkDlg = Tkinter.TkTestClass.TktestClass()
    
    tkDlg.Show()

