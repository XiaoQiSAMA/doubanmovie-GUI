from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
import sys

"""
自定义对话框
"""
class MyDialog(QDialog):

    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.edit = QLineEdit(self)
        self.edit.move(10, 10)
        button = QPushButton('发送', self)
        button.move(10, 40)
        button.clicked.connect(self.sendEditContent)
        self.setWindowTitle('MyDialog')
        self.setGeometry(300, 300, 300, 200)

    def sendEditContent(self):
        content = self.edit.text()
        self.mySignal.emit(content) # 发射信号

