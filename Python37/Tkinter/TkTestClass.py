#!/usr/bin/python
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox

class TktestClass():
    top = tkinter.Tk()
    li = ['C', 'python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']

    def helloCallBack(self):
        if tkinter.messagebox.askokcancel("Hello Python", "Hello Runoob"):
            tkinter.messagebox.showinfo("Hello showinfo", "Hello showinfo")

    def disableButtonCallBack(self):
        print("Color: ", tkinter.colorchooser.askcolor())

    def Show(self):
        button = tkinter.Button(self.top, text="点我", command=self.helloCallBack)
        button1 = tkinter.Button(self.top, text="禁用", command=self.disableButtonCallBack)
        listb = tkinter.Listbox(self.top)  # 创建两个列表组件
        listb2 = tkinter.Listbox(self.top)
        for item in self.li:  # 第一个小部件插入数据
            listb.insert(0, item)

        for item in self.movie:  # 第二个小部件插入数据
            listb2.insert(0, item)

        # 将小部件放置到主窗口中
        button.pack()
        button1.pack()
        listb.pack()
        listb2.pack()

        # 进入消息循环
        self.top.mainloop()

