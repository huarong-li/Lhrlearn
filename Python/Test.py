#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import tkinter

print("你好 python!")

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)
print(text)

top = tkinter.Tk()

# 进入消息循环
top.mainloop()