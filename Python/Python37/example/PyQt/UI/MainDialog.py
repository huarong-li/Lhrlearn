# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.setEnabled(True)
        MainDialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/en-us/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainDialog.setWindowIcon(icon)
        MainDialog.setSizeGripEnabled(True)
        MainDialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(MainDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(MainDialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 81, 31))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(MainDialog)
        self.widget.setGeometry(QtCore.QRect(260, 40, 107, 135))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.widget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.pushButton_popup = QtWidgets.QPushButton(self.widget)
        self.pushButton_popup.setObjectName("pushButton_popup")
        self.verticalLayout.addWidget(self.pushButton_popup)
        self.pushButton_custom = QtWidgets.QPushButton(self.widget)
        self.pushButton_custom.setObjectName("pushButton_custom")
        self.verticalLayout.addWidget(self.pushButton_custom)

        self.retranslateUi(MainDialog)
        self.buttonBox.accepted.connect(MainDialog.accept)
        self.buttonBox.rejected.connect(MainDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog"))
        self.label.setText(_translate("MainDialog", "TextLabel"))
        self.pushButton_start.setText(_translate("MainDialog", "Start thread"))
        self.pushButton_stop.setText(_translate("MainDialog", "End thread"))
        self.pushButton_popup.setText(_translate("MainDialog", "Popup Sys"))
        self.pushButton_custom.setText(_translate("MainDialog", "Popup custom"))
from UI import resource_rc
