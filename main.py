#! /usr/bin/env python
#coding=utf-8
import sys
sys.path+=["G:\DatabaseHomework\data"]
from Setup import *
from main_ui import*
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MyDatabase = QtGui.QWidget()
    ui = Ui_MyDatabase()
    ui.setupUi(MyDatabase)
    MyDatabase.show()
    sys.exit(app.exec_())

sys.exit(app.exec_())