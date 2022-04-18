#!/usr/bin/python
# -*- coding:utf-8 -*-

from doctest import master
import tkinter
import tkinter.messagebox
import tkinter.colorchooser
from tkinter.constants import *
import tkinter.dialog
import tkinter.simpledialog
import tkinter.commondialog

class MyDialog(tkinter.Toplevel):
    def __init__(self, master, title=None, modal=True) -> None:
        tkinter.Toplevel.__init__(self, master)
        self.transient(master)
        if title: self.title(title)
        self.minsize(width=450, height=300)
        # self.attributes('-topmost', 1)
        if modal:
            self.grab_set()

    def doModal(self):
        self.focus_set()
        self.wait_window(self)

class MyCommonDialog(tkinter.commondialog.Dialog):
    def __init__(self, master, title=None) -> None:
        tkinter.commondialog.Dialog.__init__(self, master)

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
        self.button3 = tkinter.Button(self.root, text="Second Window", command=(lambda self=self: self.onCommand_button(4)))
        self.button3.place(x=70, y=160, width=200, height=40)
        tkinter._default_root
        tkinter._cnfmerge
        print("tkinter.TkVersion: ", tkinter.TkVersion)

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
            d = tkinter.dialog.Dialog(None, {'title': 'File Modified',
                      'text':
                      'File "Python.h" has been modified'
                      ' since the last time it was saved.'
                      ' Do you want to save it before'
                      ' exiting the application.',
                      'bitmap': tkinter.dialog.DIALOG_ICON,
                      'default': 0,
                      'strings': ('Save File',
                                  'Discard Changes',
                                  'Return to Editor')})
            # d.protocol("WM_DELETE_WINDOW", d.quit)
            print(d.num)
            
            self.win_flag1.set(0)
        else:
            print("button1_command allready popup")

    def button2_command(self):
        if (self.win_flag2.get() == 0):
            self.win_flag2.set(1)
            next_win=MyDialog(self.root, "Second Window", modal=True)
            next_win.doModal()
            self.win_flag2.set(0)
        else:
            print("button2_command allready popup")
    
    def button3_command(self):
        result=tkinter.simpledialog.askinteger("dd", "sdsdss", minvalue=3, maxvalue=300, initialvalue=56)
        print(result)
    def onCommand_button(self, num):
        print(num)
        if num == 4:
            import base64
            import re
            print((base64.b64decode(base64.b64encode('Huarong'.encode('utf-8'))), 'ddd'))
            print('Huarong'.encode('utf-8'))
            _magic_re = re.compile(r'([\\{}])')
            _space_re = re.compile(r'([\s])', re.ASCII)
            match=_magic_re.search('{hh} "{height}" 54')
            print(tkinter._stringify(['[wi/dth] \hj34','{hh} "{height}" 54']))

            # dlg=MyCommonDialog(self.root, title='eee')
            # dlg.show()



class App:
    def __init__(self) -> None:
        self.root=tkinter.Tk()
        self.root.config(width=400, height=250)
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
