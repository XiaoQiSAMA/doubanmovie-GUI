import sys
from mainwindow import Ui_Window
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Ui_Window()
    main_window.show()
    sys.exit(app.exec_())