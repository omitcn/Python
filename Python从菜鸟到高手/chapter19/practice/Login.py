'''
--------《Python从菜鸟到高手》源代码------------

欧瑞科技版权所有
作者：李宁
如有任何技术问题，请加QQ技术讨论群：264268059    
或关注“极客起源”订阅号或“欧瑞科技”服务号或扫码关注订阅号和服务号，二维码在源代码根目录
如果QQ群已满，请访问https://geekori.com，在右侧查看最新的QQ群，同时可以扫码关注公众号

“欧瑞学院”是欧瑞科技旗下在线IT教育学院，包含大量IT前沿视频课程，
请访问http://geekori.com/edu或关注前面提到的订阅号和服务号，进入移动版的欧瑞学院

“极客题库”是欧瑞科技旗下在线题库，请扫描源代码根目录中的小程序码安装“极客题库”小程序

关于更多信息，请访问下面的页面
https://geekori.com/help/videocourse/readme.html



'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 206)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEditUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(190, 30, 391, 21))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(190, 70, 391, 21))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(420, 110, 71, 32))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(510, 110, 71, 32))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButtonOK.setText(_translate("MainWindow", "确定"))
        self.pushButtonCancel.setText(_translate("MainWindow", "取消"))

