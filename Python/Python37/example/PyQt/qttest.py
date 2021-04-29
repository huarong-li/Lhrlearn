#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import (QWidget, QToolTip, QDialog,
    QPushButton, QApplication, QMainWindow)
from PyQt5.QtGui import QFont

class PopupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,300)

        from PyQt5.uic import loadUi

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            print('running in a PyInstaller bundle')
            bundle_dir = sys._MEIPASS
        else:
            print('running in a normal Python process')
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
        loadUi(bundle_dir + '\\UI\\popupdialog.ui', self)
        self.pushButton.clicked.connect(self.AA)

    def AA(self):
        #s=self.label.text()
        print('....') 
 
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        
        btn.resize(btn.sizeHint())
        
        btn.move(50, 50)
        btn.clicked.connect(self.btn_click)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()

    def btn_click(self):
        print('....')
        popupdialog = PopupDialog()
        popupdialog.setModal(True)
        popupdialog.show()
        ret_value = popupdialog.exec()
        print('popupdialog.exec_()' + str(ret_value))
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
