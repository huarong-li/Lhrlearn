#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
import socket
import os

from UI.MainDialog import Ui_MainDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class PopupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,300)

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            print('running in a PyInstaller bundle')
            bundle_dir = sys._MEIPASS
        else:
            print('running in a normal Python process')
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
        re = loadUi(bundle_dir + '\\UI\\CustomDialog.ui', self, 'UI')
        if re == None:
            QMessageBox.warning(self, 'warning', 'loadUi fail')
        else:
            self.buttonBox.clicked.connect(self.AA)

    def AA(self):
        print(str(self.sender()) + '....')

class mymainwindow(QDialog, Ui_MainDialog):
    def __init__(self,parent=None):
        super(mymainwindow, self).__init__(parent)
        self.setupUi(self)

        bundle_dir = os.path.dirname(os.path.abspath(__file__))

        self.pushButton_start.clicked.connect(self.threadstartslot)
        self.pushButton_stop.clicked.connect(self.threadstopslot)
        self.pushButton_popup.clicked.connect(self.popupdailog)
        self.pushButton_custom.clicked.connect(self.popupcustomdailog)

        self.pushButton_custom.setToolTip(os.path.abspath(__file__))

    def threadstartslot(self):
        self.work = Thread()
        self.work.trigger.connect(self.deal)
        self.work.start()

    def threadstopslot(self):
        self.work.threadstartflag=False

    def popupdailog(self):
        reply=QMessageBox.information(self,"通知","程序运行时对用户操作进行反馈，保存，提交，写入等操作成功",QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        if reply == QMessageBox.Ok:
            self.label.setText('你选择了Ok！')
        else:
            self.label.setText('你选择了Close！')

    def popupcustomdailog(self):
        popupdialog = PopupDialog()
        popupdialog.setModal(True)
        popupdialog.show()
        ret = popupdialog.exec_()
        self.label.setText('popup custom dailog' + str(ret))    

    def deal(self,str):
        self.label.setText('Receive: ' + str)
        print('Receive: ' + str)

class Thread(QThread):
    trigger = pyqtSignal(str)
    def __init__(self):
        super(Thread, self).__init__()
        self.threadstartflag=True
        self.timecount=0

    def run(self):
        while self.threadstartflag == True:
            self.trigger.emit(u"计时: %d"%self.timecount)
            self.timecount+=1
            time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mymainwindow()
    MainWindow.show()
    sys.exit(app.exec_())
