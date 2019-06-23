# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog, QScrollBar, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor
from movie_info_2 import movie_info_2
from create_list import Create_List
import pymysql
from PyQt5.QtCore import pyqtSignal

mydb = pymysql.connections.Connection
print(mydb)
class Ui_Window(QMainWindow):

    def __init__(self):
        super(Ui_Window, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(955, 651)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(770, 0, 181, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, -10, 151, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 10, 381, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.send_search_data()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 54, 21))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 151, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget()
        self.verticalLayoutWidget_2.setGeometry(160, 50, 801, 601)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        # self.label_2.setStyleSheet("font-size: 25; color: red")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.setCentralWidget(self.centralwidget)
        self.pushButton_3.clicked.connect(self.push_button_3_event)
        self.pushButton_2.clicked.connect(self.push_button_2_event)
        self.pushButton.clicked.connect(self.pushButton_event)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "登陆"))
        self.toolButton_3.setText(_translate("MainWindow", "123"))
        self.toolButton_2.setText(_translate("MainWindow", "123"))
        self.toolButton.setText(_translate("MainWindow", "231"))
        self.label.setText(_translate("MainWindow", "搜索："))
        self.pushButton_2.setText(_translate("MainWindow", "电影库"))
        self.pushButton_3.setText(_translate("MainWindow", "新建列表"))
        self.label_2.setText(_translate("MainWindow", "电影信息"))



    def push_button_3_event(self):                  #新建列表
        Dialog = QtWidgets.QDialog()
        ui = Create_List()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def push_button_2_event(self):
        Dialog = Login_in_UI()
        Dialog.mySingle.connect(self.getData())

    def pushButton_event(self):                     #用户登录
        Dialog = Login_in_UI()
        Dialog.mySingle.connect(self.getData)
        Dialog.exec_()

    def getData(self, data):
        print(data)
        self.label_2.setText(data)

    def send_search_data(self):
        self.lineEdit.returnPressed.connect(self.SendData)

    def SendData(self):
        global mydb
        print(mydb)


# class MyLabel(QLabel):
#     def __init__(self,centralwidget):
# #centralwidget 窗体参数
#         super().__init__(centralwidget)
#
#         self.con(self.push_button_2_event())
#
#     def push_button_2_event(self):                  # 电影库按钮功能
#         Dialog = QtWidgets.QDialog()
#         ui = movie_info_2()
#         ui.setupUi(Dialog)
#         Dialog.show()
#         Dialog.exec_()

class Login_in_UI(QDialog):
    global mydb
    mySingle = pyqtSignal(str)

    def __init__(self):
        super(Login_in_UI,self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 80, 72, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 72, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(190, 80, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 150, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.retranslateUi()
        self.buttonBox.accepted.connect(self.mysql_connect)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名:"))
        self.label_2.setText(_translate("Dialog", "密码:"))

    def ok_click_event(self):
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if user_name == '':
            self.lineEdit.setText('请输入用户名')
        if password == '':
            self.lineEdit.setText('请输入密码')
        try:
            db = pymysql.connect('localhost', f'{user_name}', f'{password}', 'spiders')
            c = db.cursor()
            c.execute("SELECT VERSION()")
            data = c.fetchone()
            self.mySingle.emit('当前MySQL版本' + str(data))
            self.close()
            return db

        except pymysql.err.OperationalError:
            print("未连接")


    def mysql_connect(self):
        global mydb
        mydb = self.ok_click_event()







