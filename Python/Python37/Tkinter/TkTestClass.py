#!/usr/bin/python
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.colorchooser
from tkinter.constants import *

import enum
class MyEventType(str, enum.Enum):
    KeyPress = '22'
    Key = KeyPress,
    KeyRelease = '33'
    ButtonPress = '44'
    ButtonRelease = '55'
    def __str__(self) -> str:
        return self.name + '_' + self.value

class TktestClass():
    li = ['C', 'python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']
    def __init__(self) -> None:
        self.top = tkinter.Tk()

    def helloCallBack(self):
        w_mw=self.top.winfo_width()
        w_mh=self.top.winfo_height()
        if tkinter.messagebox.askokcancel("Hello Python", "Hello Runoob"):
            tkinter.messagebox.showinfo("Hello showinfo", "Hello showinfo")

    def chooseColorButtonCallBack(self):
        # print("Color: ", tkinter.colorchooser.askcolor())
        self.ShowDialog()

    def MotionCallback(self, event):
        w_mw=self.top.winfo_width()
        w_mh=self.top.winfo_height()
        # print("MotionCallback: ", event)
    
    def MapCallback(self, event):
        if (isinstance(event.widget, tkinter.Tk)):
            print('tkinter.Tk load')
            sc_w=self.top.winfo_screenwidth()
            sc_h=self.top.winfo_screenheight()
            w_mh=self.top.winfo_width()
            h_mh=self.top.winfo_height()
            x_pos=int((sc_w-w_mh)/2)
            y_pos=int((sc_h-h_mh)/2)
            self.top.geometry("{0}x{1}+{2}+{3}".format(w_mh, h_mh+2, x_pos, y_pos))
       
        print("MapCallBack", event.type, event.widget)
    
    def VisibilityCallback(self, event):
        print("VisibilityCallback", event.type, event)

    def ActivateCallback(self, event):
        print("ActivateCallback-----", event.type, event)
    
    def ButtonPressCallback(self, event):
        print("ButtonPressCallback-----", event.type, event)
    
    def ButtonReleaseCallback(self, event):
        print("ButtonReleaseCallback-----", event.type, event)

    def Show(self):
        button = tkinter.Button(self.top, text="点我", command=self.helloCallBack)
        button1 = tkinter.Button(self.top, text="选择颜色", command=self.chooseColorButtonCallBack)
        listb = tkinter.Listbox(self.top)
        listb2 = tkinter.Listbox(self.top)
        for item in self.li:
            listb.insert(0, item)

        for item in self.movie:
            listb2.insert(0, item)

        button.pack()
        button1.pack()
        listb.pack()
        listb2.pack()
        # old_geo = self.top.geometry("600x300")
        sc_w=self.top.winfo_screenwidth()
        sc_h=self.top.winfo_screenheight()
        sc_mw=self.top.winfo_screenmmwidth()
        sc_mh=self.top.winfo_screenmmheight()
        w_mh=self.top.winfo_width()
        w_mh=self.top.winfo_height()
        # self.top.resizable(True, False)
        self.top.title("Test Windows")
        self.top.minsize(250, 300)
        self.top.bind('<Motion>', func=self.MotionCallback)
        self.top.bind('<Map>', func=self.MapCallback)
        self.top.bind('<Visibility>', func=self.VisibilityCallback)
        self.top.bind('<Activate>', func=self.ActivateCallback)
        ev1=self.top.bind('<ButtonPress>', func=self.ButtonPressCallback)
        ev2=self.top.bind('<{0}>'.format(tkinter.EventType.ButtonRelease.name), func=self.ButtonReleaseCallback)
        print('<{0}>'.format(str(tkinter.EventType.ButtonRelease)))
        print('<{0}>'.format(MyEventType.Key))
        print('<{0}>'.format(MyEventType.Key.name))
        print('<{0}>'.format(MyEventType.Key.value))
        print('<{0}>'.format(str(MyEventType.Key)))

        self.top.mainloop()
    
    def ShowDialog(self):
        import tkinter.dialog
        dialog = tkinter.dialog.Dialog(self.top, title=RIDGE, text="Dialog", bitmap="questhead", default=0, strings=("OK", "Cancel"))
        print(dialog.num)
        # frame.pack(fill=BOTH,expand=1)
        # label = tkinter.Label(frame, text="Hello, World")
        # label.pack(fill=X, expand=1)
        # button = tkinter.Button(frame,text="Exit",command=self.top.destroy)
        # button.pack(side=BOTTOM)


def ShowFrame():
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text="Hello, World")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()

def ShowWith_Grid():
    tk = tkinter.Tk()

    tk.geometry('500x300+400+200')

    lable_a = tkinter.Label(tk,text='输入专辑地址：',anchor=tkinter.E)

    text_a = tkinter.Entry(tk,width=30)

    def start_download():
        print('start_download')
    btn_a = tkinter.Button(tk,text="开始",width=10,command=start_download)

    tkinter.Label(tk).grid(row=0,rowspan=5,column=1)

    lable_a.grid(row=6,column=1)

    text_a.grid(row=6,column=2)

    btn_a.grid(row=6,column=3)

    tkinter.mainloop()

def ShowWith_Place():
    tk = tkinter.Tk()

    #设置标题
    tk.title('音频下载工具')

    #设置大小位置 宽x高+左+上
    tk.geometry('500x300+400+200')

    lable_a = tkinter.Label(tk,text='输入专辑地址：',width=40,anchor=tkinter.W)

    text_a = tkinter.Entry(tk,width=40)

    def start_download():
        print('start_download')
    btn_a = tkinter.Button(tk,text="开始", width=10,command=start_download)

    lable_a.place(x=60,y=100)

    text_a.place(x=150,y=100)

    btn_a.place(x=150,y=150)

    tk.mainloop()

if __name__ == "__main__":
    tkDlg = TktestClass()
    tkDlg.Show()

    # ShowFrame()
    # ShowWith_Grid()
    # ShowWith_Place()