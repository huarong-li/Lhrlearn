#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import tkinter
import tkinter.messagebox
import tkinter.colorchooser
import Tkinter.TkTestClass


def helloCallBack():
    print("你好 python!")
    jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    text = json.loads(jsonData)
    print(text)


if __name__ == "__main__":
    tkDlg = Tkinter.TkTestClass.TktestClass()
    tkDlg.Show()

