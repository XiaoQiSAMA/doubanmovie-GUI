import sys
from GUI.mainwindow import Ui_Window
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Ui_Window()

    main_window.show()
    sys.exit(app.exec_())