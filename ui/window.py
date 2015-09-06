# -*- coding:utf-8 -*-
# file: 'windowTest'
# Create Time: '2015/9/2 20:57'
__author__ = 'Eric'

# Form implementation generated from reading ui file 'FindFile.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 397)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/search_48px.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.label_3.setObjectName("label_3")
        self.project_path = QtWidgets.QLineEdit(self.centralwidget)
        self.project_path.setGeometry(QtCore.QRect(80, 50, 311, 20))
        self.project_path.setObjectName("project_path")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label.setObjectName("label")
        self.compress_btn = QtWidgets.QPushButton(self.centralwidget)
        self.compress_btn.setGeometry(QtCore.QRect(480, 20, 61, 51))
        self.compress_btn.setStyleSheet("border-image: url(:/new/prefix1/btn.png);")
        self.compress_btn.setObjectName("compress_btn")
        self.zip_name = QtWidgets.QLineEdit(self.centralwidget)
        self.zip_name.setGeometry(QtCore.QRect(80, 20, 91, 20))
        self.zip_name.setObjectName("zip_name")
        self.file_info = QtWidgets.QLabel(self.centralwidget)
        self.file_info.setGeometry(QtCore.QRect(10, 80, 171, 16))
        self.file_info.setObjectName("file_info")
        self.open_file = QtWidgets.QToolButton(self.centralwidget)
        self.open_file.setGeometry(QtCore.QRect(400, 50, 51, 21))
        self.open_file.setObjectName("open_file")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 20, 54, 21))
        self.label_2.setObjectName("label_2")
        self.revision_max = QtWidgets.QLineEdit(self.centralwidget)
        self.revision_max.setGeometry(QtCore.QRect(380, 20, 71, 20))
        self.revision_max.setObjectName("revision_max")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 54, 21))
        self.label_5.setObjectName("label_5")
        self.revision_min = QtWidgets.QLineEdit(self.centralwidget)
        self.revision_min.setGeometry(QtCore.QRect(240, 20, 71, 20))
        self.revision_min.setObjectName("revision_min")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 531, 251))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_about = QtWidgets.QAction(MainWindow)
        self.menu_about.setObjectName("menu_about")
        self.menu_exit = QtWidgets.QAction(MainWindow)
        self.menu_exit.setObjectName("menu_exit")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.menu_about)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.menu_exit)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FindFile"))
        self.label_3.setText(_translate("MainWindow", "项目路径"))
        self.label.setText(_translate("MainWindow", "打包文件名"))
        self.compress_btn.setToolTip(_translate("MainWindow", "<html><head/><body><p>查找文件并打包</p></body></html>"))
        self.compress_btn.setText(_translate("MainWindow", "打包"))
        self.file_info.setText(_translate("MainWindow", "共0个文件"))
        self.open_file.setText(_translate("MainWindow", "浏览"))
        self.label_2.setText(_translate("MainWindow", "修订版本"))
        self.label_5.setText(_translate("MainWindow", "基础版本"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.menu_2.setTitle(_translate("MainWindow", "菜单"))
        self.menu_about.setText(_translate("MainWindow", "关于"))
        self.menu_exit.setText(_translate("MainWindow", "退出"))
        self.action.setText(_translate("MainWindow", "使用说明"))

