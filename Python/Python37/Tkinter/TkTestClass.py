#!/usr/bin/python
# -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.colorchooser

class TktestClass():
    top = tkinter.Tk()
    li = ['C', 'python', 'php', 'html', 'SQL', 'java']
    movie = ['CSS', 'jQuery', 'Bootstrap']

    def helloCallBack(self):
        w_mw=self.top.winfo_width()
        w_mh=self.top.winfo_height()
        if tkinter.messagebox.askokcancel("Hello Python", "Hello Runoob"):
            tkinter.messagebox.showinfo("Hello showinfo", "Hello showinfo")

    def chooseColorButtonCallBack(self):
        print("Color: ", tkinter.colorchooser.askcolor())

    def MotionCallback(self, event):
        w_mw=self.top.winfo_width()
        w_mh=self.top.winfo_height()
        # print("ActivateCallBack: [{0}, {1}], [{2}, {3}]".format(event.x, event.y, event.x_root, event.y_root))
    
    def MapCallback(self, event):
        if (isinstance(event.widget, tkinter.Tk)):
            print('tkinter.Tk load')
            sc_w=self.top.winfo_screenwidth()
            sc_h=self.top.winfo_screenheight()
            w_mh=self.top.winfo_width()
            h_mh=self.top.winfo_height()
            x=(int)(sc_w-w_mh)/2
            self.top.geometry("{0}x{1}+{2}+{3}".format(w_mh, h_mh+2, int((sc_w-w_mh)/2), int((sc_h-h_mh)/2)))
       
        print("MapCallBack", event.type, event.widget)
    
    def VisibilityCallback(self, event):
        print("VisibilityCallback", event.type, event.widget)

    def ActivateCallback(self, event):
        print("ActivateCallback-----", event.type, event.widget)

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
        self.top.wm_title("Test Windows")
        self.top.minsize(250, 300)
        self.top.bind('<Motion>', func=self.MotionCallback)
        self.top.bind('<Map>', func=self.MapCallback)
        self.top.bind('<Visibility>', func=self.VisibilityCallback)
        self.top.bind('<Activate>', func=self.ActivateCallback)

        # 进入消息循环
        self.top.mainloop()


if __name__ == "__main__":
    tkDlg = TktestClass()
    
    tkDlg.Show()
