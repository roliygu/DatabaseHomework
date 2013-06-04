# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sat Jun 01 18:45:23 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path+=["G:\DatabaseHomework\data"]
from Setup import *
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ex_windows2(object):
    def setupUi(self, ex_windows2):
        ex_windows2.setObjectName(_fromUtf8("ex_windows2"))
        ex_windows2.resize(354, 107)
        self.label = QtGui.QLabel(ex_windows2)
        self.label.setGeometry(QtCore.QRect(70, 30, 221, 41))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ex_windows2)
        QtCore.QMetaObject.connectSlotsByName(ex_windows2)

    def retranslateUi(self, ex_windows2):
        ex_windows2.setWindowTitle(_translate("ex_windows2", "警告", None))
        self.label.setText(_translate("ex_windows2", "请确定“年份”和“课程编码”已填写！！", None))

class Ui_ex_windows(object):
    def setupUi(self, ex_windows):
        ex_windows.setObjectName(_fromUtf8("ex_windows"))
        ex_windows.resize(268, 97)
        self.label = QtGui.QLabel(ex_windows)
        self.label.setGeometry(QtCore.QRect(60, 30, 141, 51))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(ex_windows)
        QtCore.QMetaObject.connectSlotsByName(ex_windows)

    def retranslateUi(self, ex_windows):
        ex_windows.setWindowTitle(_translate("ex_windows", "Form", None))
        self.label.setText(_translate("ex_windows", "       添加成功！", None))

class Ui_Sudent_form(object):
    def setupUi(self, Sudent_form):
        Sudent_form.setObjectName(_fromUtf8("Sudent_form"))
        Sudent_form.resize(400, 158)
        self.label = QtGui.QLabel(Sudent_form)
        self.label.setGeometry(QtCore.QRect(20, 20, 381, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Sudent_form)
        self.widget.setGeometry(QtCore.QRect(100, 50, 189, 74))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_StudentNo = QtGui.QLabel(self.widget)
        self.label_StudentNo.setObjectName(_fromUtf8("label_StudentNo"))
        self.gridLayout.addWidget(self.label_StudentNo, 0, 0, 1, 1)
        self.lineEdit_studentNo = QtGui.QLineEdit(self.widget)
        self.lineEdit_studentNo.setObjectName(_fromUtf8("lineEdit_studentNo"))
        self.gridLayout.addWidget(self.lineEdit_studentNo, 0, 1, 1, 2)
        self.label_StudentName = QtGui.QLabel(self.widget)
        self.label_StudentName.setObjectName(_fromUtf8("label_StudentName"))
        self.gridLayout.addWidget(self.label_StudentName, 1, 0, 1, 1)
        self.lineEdit_studentName = QtGui.QLineEdit(self.widget)
        self.lineEdit_studentName.setObjectName(_fromUtf8("lineEdit_studentName"))
        self.gridLayout.addWidget(self.lineEdit_studentName, 1, 1, 1, 2)
        self.label_StudentSubject = QtGui.QLabel(self.widget)
        self.label_StudentSubject.setObjectName(_fromUtf8("label_StudentSubject"))
        self.gridLayout.addWidget(self.label_StudentSubject, 2, 0, 1, 2)
        self.lineEdit_studentSubject = QtGui.QLineEdit(self.widget)
        self.lineEdit_studentSubject.setObjectName(_fromUtf8("lineEdit_studentSubject"))
        self.gridLayout.addWidget(self.lineEdit_studentSubject, 2, 2, 1, 1)
        self.widget1 = QtGui.QWidget(Sudent_form)
        self.widget1.setGeometry(QtCore.QRect(230, 130, 158, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.line_studentSubject=""
        self.line_studentNo=""
        self.line_studentName=""
        self.ex_windows = QtGui.QWidget()
        self.ui = Ui_ex_windows()
        self.ui.setupUi(self.ex_windows)
        self.k=0
        self.ui.label.setText(_translate("ex_windows", "   Student添加成功！", None))
        
        self.retranslateUi(Sudent_form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Sudent_form.close)
        QtCore.QObject.connect(self.lineEdit_studentNo, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_studentNo)
        QtCore.QObject.connect(self.lineEdit_studentSubject, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_studentSubject)
        QtCore.QObject.connect(self.lineEdit_studentName, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_studentName)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sure)
        QtCore.QMetaObject.connectSlotsByName(Sudent_form)
        
    def sure(self):
        if self.line_studentName is "" or self.line_studentNo is "" or self.studentSubject is"":
            return 0
        else :
            self.k=Add_oneclass(self.line_classNo,self.line_className,self.line_classSubject)
            self.ex_windows.show()
    
    def Sline_studentSubject(self):
        self.line_studentSubject=self.lineEdit_studentSubject.text()
    def Sline_studentNo(self):
        self.line_studentNo=self.lineEdit_studentNo.text()
    def Sline_studentName(self):
        self.line_studentName=self.lineEdit_studentName.text()
    
        

    def retranslateUi(self, Sudent_form):
        Sudent_form.setWindowTitle(_translate("Sudent_form", "Add_Student", None))
        self.label.setText(_translate("Sudent_form", "您输入的学号不存在，若想添加相关学生信息，请填写下列内容 ：", None))
        self.label_StudentNo.setText(_translate("Sudent_form", "学号 ：", None))
        self.label_StudentName.setText(_translate("Sudent_form", "姓名 ：", None))
        self.label_StudentSubject.setText(_translate("Sudent_form", "专业 ：", None))
        self.pushButton.setText(_translate("Sudent_form", "确定", None))
        self.pushButton_2.setText(_translate("Sudent_form", "取消", None))

class Ui_subject_from(object):
    def setupUi(self, subject_from):
        subject_from.setObjectName(_fromUtf8("subject_from"))
        subject_from.resize(400, 159)
        self.label = QtGui.QLabel(subject_from)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(subject_from)
        self.widget.setGeometry(QtCore.QRect(90, 50, 231, 74))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_classNo = QtGui.QLabel(self.widget)
        self.label_classNo.setObjectName(_fromUtf8("label_classNo"))
        self.gridLayout.addWidget(self.label_classNo, 0, 0, 1, 1)
        self.lineEdit_classNo = QtGui.QLineEdit(self.widget)
        self.lineEdit_classNo.setObjectName(_fromUtf8("lineEdit_classNo"))
        self.gridLayout.addWidget(self.lineEdit_classNo, 0, 1, 1, 2)
        self.label_className = QtGui.QLabel(self.widget)
        self.label_className.setObjectName(_fromUtf8("label_className"))
        self.gridLayout.addWidget(self.label_className, 1, 0, 1, 1)
        self.lineEdit_className = QtGui.QLineEdit(self.widget)
        self.lineEdit_className.setObjectName(_fromUtf8("lineEdit_className"))
        self.gridLayout.addWidget(self.lineEdit_className, 1, 1, 1, 2)
        self.label_classSubject = QtGui.QLabel(self.widget)
        self.label_classSubject.setObjectName(_fromUtf8("label_classSubject"))
        self.gridLayout.addWidget(self.label_classSubject, 2, 0, 1, 2)
        self.lineEdit_classSubject = QtGui.QLineEdit(self.widget)
        self.lineEdit_classSubject.setObjectName(_fromUtf8("lineEdit_classSubject"))
        self.gridLayout.addWidget(self.lineEdit_classSubject, 2, 2, 1, 1)
        self.widget1 = QtGui.QWidget(subject_from)
        self.widget1.setGeometry(QtCore.QRect(230, 130, 158, 25))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget1)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.ex_windows = QtGui.QWidget()
        self.ui = Ui_ex_windows()
        self.ui.setupUi(self.ex_windows)
        self.line_classNo=""
        self.line_className=""
        self.line_classSubject=""
        self.k=0
        self.ui.label.setText(_translate("ex_windows", "   Class添加成功！", None))
        
        self.retranslateUi(subject_from)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), subject_from.close)
        QtCore.QObject.connect(self.lineEdit_classNo, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_classNo)
        QtCore.QObject.connect(self.lineEdit_className, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_className)
        QtCore.QObject.connect(self.lineEdit_classSubject, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_classSubject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sure)
        QtCore.QMetaObject.connectSlotsByName(subject_from)
    
    def sure(self):
        if self.line_className is "" or self.line_classNo is "" or self.line_classSubject is"":
            return 0
        else :
            self.k=Add_oneclass(self.line_classNo,self.line_className,self.line_classSubject)
            self.ex_windows.show()
    def Sline_classNo(self):
        self.line_classNo=self.lineEdit_classNo.text()
    def Sline_className(self):
        self.line_className=self.lineEdit_className.text()
    def Sline_classSubject(self):
        self.line_classSubject=self.lineEdit_classSubject.text()
        
    
        

    def retranslateUi(self, subject_from):
        subject_from.setWindowTitle(_translate("subject_from", "Add_Newclass", None))
        self.label.setText(_translate("subject_from", "您输入的课程编号不存在，若想添加相关课程信息，请在填写下列内容：", None))
        self.label_classNo.setText(_translate("subject_from", "课程编号 ：", None))
        self.label_className.setText(_translate("subject_from", "课程名称 ：", None))
        self.label_classSubject.setText(_translate("subject_from", "课程所属专业 ：", None))
        self.pushButton.setText(_translate("subject_from", "确定", None))
        self.pushButton_2.setText(_translate("subject_from", "取消", None))

class Ui_MyDatabase(object):
    def setupUi(self, MyDatabase):
        MyDatabase.setObjectName(_fromUtf8("MyDatabase"))
        MyDatabase.resize(724, 519)
        self.groupBox = QtGui.QGroupBox(MyDatabase)
        self.groupBox.setGeometry(QtCore.QRect(40, 40, 641, 461))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tabWidget = QtGui.QTabWidget(self.groupBox)
        self.tabWidget.setGeometry(QtCore.QRect(30, 70, 581, 371))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_Add = QtGui.QWidget()
        self.tab_Add.setObjectName(_fromUtf8("tab_Add"))
        self.layoutWidget = QtGui.QWidget(self.tab_Add)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 50, 219, 48))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_studentNum = QtGui.QLabel(self.layoutWidget)
        self.label_studentNum.setObjectName(_fromUtf8("label_studentNum"))
        self.gridLayout_2.addWidget(self.label_studentNum, 0, 0, 1, 1)
        self.lineEdit_studentNum = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_studentNum.setObjectName(_fromUtf8("lineEdit_studentNum"))
        self.gridLayout_2.addWidget(self.lineEdit_studentNum, 0, 1, 1, 1)
        self.label__grade = QtGui.QLabel(self.layoutWidget)
        self.label__grade.setObjectName(_fromUtf8("label__grade"))
        self.gridLayout_2.addWidget(self.label__grade, 1, 0, 1, 1)
        self.lineEdit_grade = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_grade.setObjectName(_fromUtf8("lineEdit_grade"))
        self.gridLayout_2.addWidget(self.lineEdit_grade, 1, 1, 1, 1)
        self.pushButton_ok = QtGui.QPushButton(self.tab_Add)
        self.pushButton_ok.setGeometry(QtCore.QRect(470, 300, 75, 23))
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.label_inputMul = QtGui.QLabel(self.tab_Add)
        self.label_inputMul.setGeometry(QtCore.QRect(90, 150, 71, 16))
        self.label_inputMul.setObjectName(_fromUtf8("label_inputMul"))
        self.textEdit_inputMul = QtGui.QTextEdit(self.tab_Add)
        self.textEdit_inputMul.setGeometry(QtCore.QRect(180, 150, 281, 131))
        self.textEdit_inputMul.setObjectName(_fromUtf8("textEdit_inputMul"))
        self.pushButton_open = QtGui.QPushButton(self.tab_Add)
        self.pushButton_open.setGeometry(QtCore.QRect(380, 300, 75, 23))
        self.pushButton_open.setObjectName(_fromUtf8("pushButton_open"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_Add)
        self.layoutWidget1.setGeometry(QtCore.QRect(480, 20, 73, 40))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_inputMul = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox_inputMul.setObjectName(_fromUtf8("checkBox_inputMul"))
        self.verticalLayout_2.addWidget(self.checkBox_inputMul)
        self.tabWidget.addTab(self.tab_Add, _fromUtf8(""))
        self.tab_Search = QtGui.QWidget()
        self.tab_Search.setObjectName(_fromUtf8("tab_Search"))
        self.tableWidget = QtGui.QTableWidget(self.tab_Search)
        self.tableWidget.setGeometry(QtCore.QRect(60, 30, 441, 271))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(30)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(25, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(26, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(27, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(28, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(29, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_show = QtGui.QPushButton(self.tab_Search)
        self.pushButton_show.setGeometry(QtCore.QRect(470, 310, 75, 23))
        self.pushButton_show.setObjectName(_fromUtf8("pushButton_show"))
        self.tabWidget.addTab(self.tab_Search, _fromUtf8(""))
        self.layoutWidget2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(330, 20, 285, 50))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_year = QtGui.QLabel(self.layoutWidget2)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.verticalLayout.addWidget(self.label_year)
        self.label_subjectName = QtGui.QLabel(self.layoutWidget2)
        self.label_subjectName.setObjectName(_fromUtf8("label_subjectName"))
        self.verticalLayout.addWidget(self.label_subjectName)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_year = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_year.setObjectName(_fromUtf8("lineEdit_year"))
        self.gridLayout.addWidget(self.lineEdit_year, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.lineEdit_subjectName = QtGui.QLineEdit(self.layoutWidget2)
        self.lineEdit_subjectName.setObjectName(_fromUtf8("lineEdit_subjectName"))
        self.gridLayout.addWidget(self.lineEdit_subjectName, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.checkBox_SQL_k=False
        self.checkBox_inputMul_k=False
        self.retranslateUi(MyDatabase)
        self.tabWidget.setCurrentIndex(0)
        self.line_year=""
        self.line_subjectName=""
        self.line_studentNum=""
        self.line_grade=""
        self.text=[]
        self.ex_text=""
        
        self.ex_windows = QtGui.QWidget()
        self.ui1 = Ui_ex_windows()
        self.ui1.setupUi(self.ex_windows)
        
        self.ex_windows2 = QtGui.QWidget()
        self.ui2 = Ui_ex_windows2()
        self.ui2.setupUi(self.ex_windows2)
        
        self.Sudent_form = QtGui.QWidget()
        self.ui3 = Ui_Sudent_form()
        self.ui3.setupUi(self.Sudent_form)
        
        self.subject_from = QtGui.QWidget()
        self.ui4 = Ui_subject_from()
        self.ui4.setupUi(self.subject_from)
        
        
        self.retranslateUi(MyDatabase)
        self.tabWidget.setCurrentIndex(1)
        
        QtCore.QObject.connect(self.pushButton_open, QtCore.SIGNAL(_fromUtf8("clicked()")), self.file_open)
        QtCore.QObject.connect(self.pushButton_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sure)
        QtCore.QMetaObject.connectSlotsByName(MyDatabase)
        QtCore.QObject.connect(self.pushButton_show, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showup)
        QtCore.QObject.connect(self.checkBox_inputMul, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkBox_inputMul_bool)
        QtCore.QObject.connect(self.lineEdit_year, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_year)
        QtCore.QObject.connect(self.lineEdit_subjectName, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_subjectName)
        QtCore.QObject.connect(self.lineEdit_studentNum, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_studentNum)
        QtCore.QObject.connect(self.lineEdit_grade, QtCore.SIGNAL(_fromUtf8("editingFinished()")), self.Sline_grade)
        
    def sure(self):
        if self.checkBox_inputMul_k is True :
            self.ex_text=self.textEdit_inputMul.toPlainText()
            self.text=self.ex_text.split('\n')
            Add_mul(self.text)
            self.ex_windows.show()
        elif self.checkBox_inputMul_k is False :
            Add_one(self.line_grade,self.line_studentNum,self.line_subjectName,self.line_year)
            self.ex_windows.show()
    def checkBox_inputMul_bool(self):
        self.checkBox_inputMul_k=self.checkBox_inputMul.isChecked()
    def Sline_year(self):
        self.line_year=self.lineEdit_year.text()
    def Sline_subjectName(self):
        self.line_subjectName=self.lineEdit_subjectName.text()
    def Sline_studentNum(self):
        self.line_studentNum=self.lineEdit_studentNum.text()
    def Sline_grade(self):
        self.line_grade=self.lineEdit_grade.text()
    def showup(self):
        if self.line_subjectName not in get_allclassID():
            self.subject_from.show()
            return 0
        if self.line_year is "" or self.line_subjectName is "":
            self.ex_windows2.show()
            return 0
        for x in range(0,31):
            for y in range(0,5):
                item = QtGui.QTableWidgetItem(" ")
                self.tableWidget.setItem(x,y,item)
        T=get_all(self.line_year,self.line_subjectName)
        j=0
        for i in T:
            item = QtGui.QTableWidgetItem(T[j][0])
            self.tableWidget.setItem(j,0,item)
                
            a=""
            a=self.line_subjectName
            item = QtGui.QTableWidgetItem(a)
            self.tableWidget.setItem(j,1,item)
                
            c=str(T[j][1])
            item = QtGui.QTableWidgetItem(c)
            self.tableWidget.setItem(j,2,item)
                
            b=""
            b=self.line_year
            item = QtGui.QTableWidgetItem(b)
            self.tableWidget.setItem(j,3,item)
            j+=1
    
    def file_open(self):
        fd = QtGui.QFileDialog()
        plik = open(fd.getOpenFileName()).read()
        self.textEdit_inputMul.setText(plik)
    
    def retranslateUi(self, MyDatabase):
        MyDatabase.setWindowTitle(_translate("MyDatabase", "Form", None))
        self.groupBox.setTitle(_translate("MyDatabase", "Box", None))
        self.label_studentNum.setText(_translate("MyDatabase", "  输入学号 ：", None))
        self.label__grade.setText(_translate("MyDatabase", "  输入成绩 ：", None))
        self.pushButton_ok.setText(_translate("MyDatabase", "确定", None))
        self.label_inputMul.setText(_translate("MyDatabase", " 批量输入 ：", None))
        self.pushButton_open.setText(_translate("MyDatabase", "打开", None))
        self.checkBox_inputMul.setText(_translate("MyDatabase", "批量输入", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Add), _translate("MyDatabase", "Add", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MyDatabase", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MyDatabase", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MyDatabase", "3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MyDatabase", "4", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MyDatabase", "5", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MyDatabase", "6", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MyDatabase", "7", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MyDatabase", "8", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MyDatabase", "9", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MyDatabase", "10", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MyDatabase", "11", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MyDatabase", "12", None))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MyDatabase", "13", None))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MyDatabase", "14", None))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MyDatabase", "15", None))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MyDatabase", "16", None))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MyDatabase", "17", None))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MyDatabase", "18", None))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MyDatabase", "19", None))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("MyDatabase", "20", None))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("MyDatabase", "21", None))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("MyDatabase", "22", None))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("MyDatabase", "23", None))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("MyDatabase", "24", None))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("MyDatabase", "25", None))
        item = self.tableWidget.verticalHeaderItem(25)
        item.setText(_translate("MyDatabase", "26", None))
        item = self.tableWidget.verticalHeaderItem(26)
        item.setText(_translate("MyDatabase", "27", None))
        item = self.tableWidget.verticalHeaderItem(27)
        item.setText(_translate("MyDatabase", "28", None))
        item = self.tableWidget.verticalHeaderItem(28)
        item.setText(_translate("MyDatabase", "29", None))
        item = self.tableWidget.verticalHeaderItem(29)
        item.setText(_translate("MyDatabase", "30", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MyDatabase", "学号", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MyDatabase", "课程编号", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MyDatabase", "成绩", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MyDatabase", "年份", None))
        self.pushButton_show.setText(_translate("MyDatabase", "查找", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Search), _translate("MyDatabase", "Search", None))
        self.label_year.setText(_translate("MyDatabase", "年份 ：", None))
        self.label_subjectName.setText(_translate("MyDatabase", "课程编号 ：", None))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex_windows = QtGui.QWidget()
    ui = Ui_ex_windows()
    ui.setupUi(ex_windows)
    MyDatabase = QtGui.QWidget()
    ui = Ui_MyDatabase()
    ui.setupUi(MyDatabase)
    MyDatabase.show()
    sys.exit(app.exec_())

   
