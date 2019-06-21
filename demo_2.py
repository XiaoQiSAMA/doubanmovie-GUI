from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from demo import MyDialog
import sys
"""
主窗口
"""
class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('open', self)
        self.button.clicked.connect(self.openMyDialog)
        self.button.move(10, 10)
        self.label = QLabel("hello", self)
        self.label.move(10, 50)
        self.setWindowTitle('Window')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def openMyDialog(self):
        my = MyDialog(self)
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignal)
        my.exec_()

    """
    实现槽函数
    """
    def getDialogSignal(self, connect):
        self.label.setText(connect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    sys.exit(app.exec_())