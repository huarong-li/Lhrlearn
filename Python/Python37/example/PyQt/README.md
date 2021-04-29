# Lhrlearn

PyQt5使用
需要下载库以及工具
pip install PyQt5
pip install pyqt5-tools

QT5-GUI设计器的使用
用命令打开设计器   pyqt5-tools designer

使用 pyuic5 将.ui文件转换为py文件
使用 pyrcc5 将.qrc文件转换为py文件

示例：
pyuic5 .\MainDialog.ui -o .\MainDialog.py --import-from=UI
pyrcc5 .\resource.qrc -o .\resource_rc.py
