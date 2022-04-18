#!/usr/bin/python
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.colorchooser
from tkinter.constants import *

class MyDialog(tkinter.Toplevel):
    def __init__(self, master, title=None, modal=True) -> None:
        tkinter.Toplevel.__init__(self, master)
        self.transient(master)
        if title: self.title(title)
        self.minsize(width=450, height=300)
        # self.attributes('-topmost', 1)
        if modal:
            self.grab_set()
        self.focus_set()
        self.wait_window(self)

class MainWindow:
    def __init__(self, parent) -> None:
        self.root=parent
        self.win_flag1=tkinter.IntVar(self.root, 0)
        self.win_flag2=tkinter.IntVar(self.root, 0)
        self._winflag=None
        self.initWidgets()
    
    def initWidgets(self):
        self.button1 = tkinter.Button(self.root, text="First Window", command=self.button1_command)
        self.button1.place(x=70, y=40, width=200, height=40)
        self.button2 = tkinter.Button(self.root, text="Second Window", command=self.button2_command)
        self.button2.place(x=70, y=100, width=200, height=40)

    def onActivate(self):
        print(locals().keys())
        print(self.__dict__.keys())
        print('root' in self.__dict__.keys())
        print('root1' in self.__dict__.keys())
        if ('root' in self.__dict__.keys() and isinstance(self.root, tkinter.Tk)):
            for k, v in self.__dict__.items():
                print(k, v)
            for k in self.__dict__.keys():
                print(k)
            for k in self.__dict__.values():
                print(k)
            for k in self.__dict__:
                print(k)

    def button1_command(self):
        if (self.win_flag1.get() == 0):
            self.win_flag1.set(1)
            next_win=MyDialog(self.root, "First Window")
            self.win_flag1.set(0)
        else:
            print("button1_command allready popup")

    def button2_command(self):
        if (self.win_flag2.get() == 0):
            self.win_flag2.set(1)
            next_win=MyDialog(self.root, "Second Window", modal=False)
            self.win_flag2.set(0)
        else:
            print("button2_command allready popup")

class App:
    def __init__(self) -> None:
        self.root=tkinter.Tk()
        self.root.config(width=400, height=200)
        self.root.title("Multi Windows Demo")
        self._main_Frame=MainWindow(self.root)
    def OnLaunched(self):
        self._main_Frame.onActivate()
        self.root.mainloop()
    def GetMainFrame(self):
        return self.root

if __name__ == "__main__":
    app=App()

    app.OnLaunched()
