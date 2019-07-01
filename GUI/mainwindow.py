from PyQt5.QtWidgets import QPushButton, QMessageBox
# from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QMenu, QAction, QLabel, QHBoxLayout, QLineEdit
from GUI.movie_info_2 import movie_info_2
# from create_list import Create_List
from PyQt5.QtGui import QIcon, QCursor
import pymysql
from PyQt5.QtCore import pyqtSignal, Qt

mydb = pymysql.connections.Connection
page_status = 0
count = 0
likes = 0
page = 0
do_search = 0
likes_page = 0


def search_by_id(id):  # 用来搜索显示在按钮上的电影信息
    global mydb
    global page_status
    global likes
    global likes_page
    try:
        cursor = mydb.cursor()
    except TypeError:
        pass
    if page_status == 1:
        sql = 'SELECT id,name,daoyan FROM spiders.movies where id = ' + str(id)
        cursor.execute(sql)
        result = list(cursor.fetchall()[0])
    elif page_status == 2:
        print('likes is ', likes)
        print('likes_page is', likes_page)
        if likes >= id:
            sql = 'SELECT shoucang.id,name,daoyan FROM spiders.movies,spiders.shoucang where  spiders.shoucang.id=' + str(
                id) + ' and  spiders.movies.id = spiders.shoucang.moviesid'
            cursor.execute(sql)
            result = list(cursor.fetchall()[0])
        else:
            result = []
    # print(result)
    return result


def get_details():  # 获取按钮上的电影信息
    global page
    global count
    global page_status
    global likes_page
    details = []
    for i in range(1, 11):
        if page_status == 1:
            id = page * 10 + i
            if id > count:
                details.append([])
            else:
                details.extend([search_by_id(id)])
        else:
            id = likes_page * 10 + i
            if id > likes:
                print('id =', id, 'likes=', likes)
                details.append([])
            else:
                details.extend([search_by_id(id)])

    print('details', details)
    return details


class Ui_Window(QMainWindow):
    global count

    control_signal = pyqtSignal(list)

    def __init__(self):
        super(Ui_Window, self).__init__()
        self.setupUi()
        icon = QIcon('dio.jpg')
        self.setWindowIcon(icon)
        self.control_signal.connect(self.page_controller)
        self.setPageController()  # 将选页的按钮加载出来


    def setupUi(self):
        global count
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(C:/Users/xiaoqi/Documents/Python_Spider_mysql/images/bg.jpg)}")
        self.resize(955, 651)
        self.setFixedSize(self.width(), self.height())
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
        # self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        # self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, -10, 151, 61))
        # self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        # self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.toolButton_3 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        # self.toolButton_3.setObjectName("toolButton_3")
        # self.horizontalLayout_2.addWidget(self.toolButton_3)
        # self.toolButton_2 = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        # self.toolButton_2.setObjectName("toolButton_2")
        # self.horizontalLayout_2.addWidget(self.toolButton_2)
        # self.toolButton = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        # self.toolButton.setObjectName("toolButton")
        # self.horizontalLayout_2.addWidget(self.toolButton)
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 50, 801, 601))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.button_1 = Btn_Single(1)
        self.verticalLayout_2.addWidget(self.button_1)
        self.button_1.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_2 = Btn_Single(2)
        self.verticalLayout_2.addWidget(self.button_2)
        self.button_2.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_3 = Btn_Single(3)
        self.verticalLayout_2.addWidget(self.button_3)
        self.button_3.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_4 = Btn_Single(4)
        self.verticalLayout_2.addWidget(self.button_4)
        self.button_4.setStyleSheet("font-size: 22px; background: transparent;text-align: left;")
        self.button_5 = Btn_Single(5)
        self.verticalLayout_2.addWidget(self.button_5)
        self.button_5.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_6 = Btn_Single(6)
        self.verticalLayout_2.addWidget(self.button_6)
        self.button_6.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_7 = Btn_Single(7)
        self.verticalLayout_2.addWidget(self.button_7)
        self.button_7.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_8 = Btn_Single(8)
        self.verticalLayout_2.addWidget(self.button_8)
        self.button_8.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_9 = Btn_Single(9)
        self.verticalLayout_2.addWidget(self.button_9)
        self.button_9.setStyleSheet("font-size: 22px;background: transparent;text-align: left;")
        self.button_10 = Btn_Single(10)
        self.verticalLayout_2.addWidget(self.button_10)
        self.button_10.setStyleSheet("font-style:bold;font-size: 22px;background: transparent;text-align: left;")
        self.setCentralWidget(self.centralwidget)

        self.pushButton_3.clicked.connect(self.increase_shoucang_list)
        self.pushButton_2.clicked.connect(self.increase_pool_list)
        self.pushButton.clicked.connect(self.pushButton_event)
        # self.toolButton.clicked.connect(self.toolButton_event)
        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)

    def setPageController(self):
        global count
        """自定义页码控制器"""
        control_layout = QHBoxLayout()
        homePage = QPushButton("首页")
        prePage = QPushButton("<上一页")
        self.curPage = QLabel("1")
        nextPage = QPushButton("下一页>")
        finalPage = QPushButton("尾页")
        self.totalPage = QLabel("共" + str(0) + "页")
        skipLable_0 = QLabel("跳到")
        self.skipPage = QLineEdit()
        skipLabel_1 = QLabel("页")
        confirmSkip = QPushButton("确定")
        homePage.clicked.connect(self.__home_page)
        prePage.clicked.connect(self.__pre_page)
        nextPage.clicked.connect(self.__next_page)
        finalPage.clicked.connect(self.__final_page)
        confirmSkip.clicked.connect(self.__confirm_skip)
        control_layout.addStretch(1)
        control_layout.addWidget(homePage)
        control_layout.addWidget(prePage)
        control_layout.addWidget(self.curPage)
        control_layout.addWidget(nextPage)
        control_layout.addWidget(finalPage)
        control_layout.addWidget(self.totalPage)
        control_layout.addWidget(skipLable_0)
        control_layout.addWidget(self.skipPage)
        control_layout.addWidget(skipLabel_1)
        control_layout.addWidget(confirmSkip)
        control_layout.addStretch(1)
        self.verticalLayout_2.addLayout(control_layout)

    def __home_page(self):
        """点击首页信号"""
        self.control_signal.emit(["home", self.curPage.text()])

    def __pre_page(self):
        """点击上一页信号"""
        self.control_signal.emit(["pre", self.curPage.text()])

    def __next_page(self):
        """点击下一页信号"""
        self.control_signal.emit(["next", self.curPage.text()])

    def __final_page(self):
        """尾页点击信号"""
        self.control_signal.emit(["final", self.curPage.text()])

    def __confirm_skip(self):
        """跳转页码确定"""
        self.control_signal.emit(["confirm", self.skipPage.text()])

    def showTotalPage(self):
        """返回当前总页数"""
        print('返回当前总页数', self.totalPage.text())
        return int(self.totalPage.text()[1:-1])

    def increase_pool_list(self):  # 讲获取到的按钮上的电影信息发送至按钮
        global mydb
        global page
        global do_search
        global page_status
        global count
        global likes
        global likes_page
        cursor = mydb.cursor()
        cursor.execute('select count(*) from spiders.movies')
        count = int(cursor.fetchall()[0][0])

        self.totalPage.setText("共" + str(int(count / 10) + 1) + "页")
        self.curPage.setText('1')
        page_status = 1
        page = 0
        do_search = 0
        details = get_details()
        self.SendData(details)

    def increase_shoucang_list(self):  # 讲获取到的按钮上的电影信息发送至按钮
        global page
        global do_search
        global page_status
        global count
        global likes
        global likes_page
        cursor = mydb.cursor()
        cursor.execute('select count(*) from spiders.shoucang')
        likes = int(cursor.fetchall()[0][0])
        self.totalPage.setText("共" + str(int(likes / 10) + 1) + "页")
        self.curPage.setText('1')
        page_status = 2
        likes_page = 0
        do_search = 0
        details = get_details()
        self.SendData(details)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "登陆"))
        # self.toolButton_3.setText(_translate("MainWindow", ""))
        # self.toolButton_2.setText(_translate("MainWindow", "123"))
        # self.toolButton.setText(_translate("MainWindow", "快捷登录"))
        self.label.setText(_translate("MainWindow", "搜索："))
        self.pushButton_2.setText(_translate("MainWindow", "电影库"))
        self.pushButton_3.setText(_translate("MainWindow", "收藏列表"))

        self.ten_button_text = [
            self.button_1.setText,
            self.button_2.setText,
            self.button_3.setText,
            self.button_4.setText,
            self.button_5.setText,
            self.button_6.setText,
            self.button_7.setText,
            self.button_8.setText,
            self.button_9.setText,
            self.button_10.setText
        ]

    # def push_button_3_event(self):  # 新建列表
    #     global page
    #     global do_search
    #     do_search = 0
    #     Dialog = QtWidgets.QDialog()
    #     ui = Create_List()
    #     ui.setupUi(Dialog)
    #     Dialog.show()
    #     Dialog.exec_()

    def pushButton_event(self):  # 用户登录
        Dialog = Login_in_UI()
        Dialog.mySingle.connect(self.getData)

        Dialog.exec_()

    # def toolButton_event(self):  # 测试用的登录按钮231
    #     global mydb
    #     global count
    #     mydb = pymysql.connect('localhost', 'root', '990701', 'spiders')
    #     cursor = mydb.cursor()
    #     sql = 'SELECT count(*) FROM spiders.movies'
    #     cursor.execute(sql)
    #     count = cursor.fetchall()[0][0]
    #
    #     # print(count)

    def getData(self):
        # print(data)
        self.pushButton.setText('已登录')

    def send_search_data(self):  # 发送搜索框的字符串
        self.lineEdit.returnPressed.connect(self.return_search_info)

    def return_search_info(self):
        global do_search
        try:
            cursor = mydb.cursor()
            cursor.execute(f"select id from spiders.movies where name='{self.lineEdit.text()}'")
            info = list(cursor.fetchall()[0])
            info = str(info[0])
            do_search = info
            mdetails = [search_by_id(info), '', '', '', '', '', '', '', '', '']
            self.SendData(mdetails)
        except:
            QMessageBox.warning(self, '警告', '未找到！')


    def SendData(self, results):  # 电影库列表数据
        # print('results len is ', len(results))
        for i in range(len(self.ten_button_text)):
            if i < len(results):
                if results[i]:
                    results[i][0] = str(results[i][0])
                    infor = ' '.join(results[i])
                    # print(infor)
                    self.ten_button_text[i](infor)
                else:
                    self.ten_button_text[i]('')
            else:
                # self.ten_button_text[i]('')
                pass

    def page_controller(self, signal):
        global page
        global likes_page
        global page_status
        total_page = self.showTotalPage()
        if "home" == signal[0]:
            self.curPage.setText("1")
            if page_status == 1:
                page = 0
            else:
                likes_page = 0
            details = get_details()
            self.SendData(details)
        elif "pre" == signal[0]:
            try:
                if 1 == int(signal[1]):
                    QMessageBox.information(self, "提示", "已经是第一页了", QMessageBox.Yes)
                    return

                if page_status:
                    self.curPage.setText(str(int(signal[1]) - 1))
                    if page_status == 1:
                        page = page - 1
                    elif page_status == 2:
                        likes_page = likes_page - 1
                    details = get_details()
                    self.SendData(details)
                else:
                    pass

            except UnboundLocalError:
                QMessageBox.warning(self, '警告', '你没有初始化电影库！')


        elif "next" == signal[0]:
            if total_page == int(signal[1]):
                QMessageBox.information(self, "提示", "已经是最后一页了", QMessageBox.Yes)
                return

            if page_status:
                self.curPage.setText(str(int(signal[1]) + 1))
                if page_status == 1:
                    page = page + 1
                elif page_status == 2:
                    likes_page = likes_page + 1
                details = get_details()
                self.SendData(details)
            else:
                pass

        elif "final" == signal[0]:
            try:

                if page_status:
                    self.curPage.setText(str(total_page))
                    if page_status == 1:
                        page = total_page - 1
                    elif page_status == 2:
                        likes_page = total_page - 1
                    details = get_details()
                    self.SendData(details)
                else:
                    pass


            except:
                QMessageBox.warning(self, '警告', '你没有初始化电影库！')



        elif "confirm" == signal[0]:
            try:
                if total_page < int(signal[1]) or int(signal[1]) <= 0:
                    QMessageBox.information(self, "提示", "跳转页码超出范围", QMessageBox.Yes)
                    return
                self.curPage.setText(signal[1])
                if page_status == 1:
                    page = int(signal[1]) - 1
                else:
                    likes_page = int(signal[1]) - 1

                details = get_details()
                self.SendData(details)
            except ValueError:
                pass


class Login_in_UI(QDialog):
    global mydb
    mySingle = pyqtSignal(str)

    def __init__(self):
        super(Login_in_UI, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 子窗口阻塞父窗口
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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
        global mydb
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            mydb = pymysql.connect('localhost', f'{user_name}', f'{password}', 'spiders')
            self.close()
            print("数据库连接成功")
        except pymysql.err.OperationalError:
            QMessageBox.warning(self, '错误', '账号或密码错误！')

    def mysql_connect(self):
        global mydb
        global count
        self.ok_click_event()
        try:
            cursor = mydb.cursor()
            sql = 'SELECT count(*) FROM spiders.movies'
            cursor.execute(sql)
            count = cursor.fetchall()[0][0]
        except AttributeError:
            pass


#
class Btn_Single(QPushButton):
    btn_single = pyqtSignal(int)

    def __init__(self, id):
        self.id = id
        super(Btn_Single, self).__init__()
        self.clicked.connect(self.Btn_text)
        self.btn_single.connect(self.Btn_Songle_clicked_event)
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

    def contextMenuEvent(self):
        global page_status
        if not page_status:
            self.isEnabled()
        else:
            self.isVisible()
            popMenu = QMenu()
            if page_status == 1:
                action1 = popMenu.addAction(u'收藏')
                action1.triggered.connect(self.shoucang)
            else:
                action2 = popMenu.addAction(u'取消收藏')
                action2.triggered.connect(self.quxiao)
            print(type(id))
            popMenu.exec_(QCursor.pos())

    def shoucang(self):
        global page
        global likes
        id = page * 10 + self.id
        print(id)
        cursor = mydb.cursor()
        try:
            if cursor.execute(f'insert into shoucang(moviesid) value({id})'):
                print('收藏succ')
                mydb.commit()

                cursor.execute('select * from shoucang')
                result = cursor.fetchall()
                likes = likes - 1
                numbers = []
                long = len(result)
                for item in result:
                    numbers.append(item[0])
                print('numbers is', numbers)
                for i in range(100000 + 1, 100000 + long + 1):
                    print('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 100000 - 1]))
                    cursor.execute('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 100000 - 1]))
                    mydb.commit()

                cursor.execute('select * from shoucang')
                result = cursor.fetchall()
                likes = likes - 1
                numbers = []
                long = len(result)
                for item in result:
                    numbers.append(item[0])
                print('numbers is', numbers)
                for i in range(1, long + 1):
                    print('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 1]))
                    cursor.execute('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 1]))
                    mydb.commit()
            else:
                print('收藏fail')
                mydb.rollback()
        except:
            print("收藏次数过多")
            pass

    def quxiao(self):
        global page
        global likes
        id = page * 10 + self.id
        print(id)
        cursor = mydb.cursor()
        # try:
        if cursor.execute(f'delete  from shoucang where id = {id}'):
            print('取消收藏succ')
            mydb.commit()

            cursor.execute('select * from shoucang')
            result = cursor.fetchall()
            likes = likes - 1
            numbers = []
            long = len(result)
            for item in result:
                numbers.append(item[0])
            print('numbers is', numbers)
            for i in range(100000 + 1, 100000 + long + 1):
                print('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 100000 - 1]))
                cursor.execute('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 100000 - 1]))
                mydb.commit()

            cursor.execute('select * from shoucang')
            result = cursor.fetchall()
            likes = likes - 1
            numbers = []
            long = len(result)
            for item in result:
                numbers.append(item[0])
            print('numbers is', numbers)
            for i in range(1, long + 1):
                print('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 1]))
                cursor.execute('update shoucang set id = ' + str(i) + ' where id=' + str(numbers[i - 1]))
                mydb.commit()

            # 刷新页面

        else:
            mydb.rollback()
            print('取消收藏fail')
        # except:
        #     print("取消收藏错误")
        #     pass

        # def processtrigger(self):
        #
        #     if q.text() == '收藏':
        #         cursor = mydb.cursor()
        #         if cursor.execute('insert into shoucang value(moviesid = {})'.format(id)):
        #             print('收藏succ')
        #         else:
        #             print('收藏fail')
        #     elif q.text() == '删除':
        #         cursor = mydb.cursor()
        #         if cursor.execute('DELETE FROM movies WHERE id={}'.format(id)):
        #             print('删除succ')
        #         else:
        #             print('删除fail')
        #     else:
        #         cursor = mydb.cursor()
        #         if cursor.execute('DELETE FROM shoucang WHERE id={}'.format(id)):
        #             print('取消收藏succ')
        #         else:
        #             print('取消收藏fail')

    def Btn_text(self):
        self.btn_single.emit(self.id)

    def Btn_Songle_clicked_event(self, id):  # ten botton 按钮功能 只更改detali页面内容
        global mydb
        global page
        global do_search
        global likes_page
        global page_status
        Dialog = movie_info_2()
        try:
            if do_search:
                if id == 1:
                    id = do_search
                    Dialog.set_value(id, mydb)
                    Dialog.show()
                    Dialog.exec_()

            else:
                if page_status == 1:

                    id = page * 10 + id
                    Dialog.set_value(id, mydb)
                    Dialog.show()
                    Dialog.exec_()
                elif page_status == 2:
                    id = likes_page * 10 + id
                    cursor = mydb.cursor()
                    cursor.execute('select moviesid from spiders.shoucang where id = ' + str(id))
                    id = cursor.fetchall()[0][0]
                    Dialog.set_value(id, mydb)
                    Dialog.show()
                    Dialog.exec_()
        except IndexError:
            pass
