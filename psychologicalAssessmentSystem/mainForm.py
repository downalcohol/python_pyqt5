# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_chatting = QtWidgets.QWidget()
        self.page_chatting.setObjectName("page_chatting")
        self.text_msgBrowser = QtWidgets.QTextBrowser(self.page_chatting)
        self.text_msgBrowser.setGeometry(QtCore.QRect(5, 0, 990, 620))
        self.text_msgBrowser.setObjectName("text_msgBrowser")
        self.widget = QtWidgets.QWidget(self.page_chatting)
        self.widget.setGeometry(QtCore.QRect(0, 260, 500, 121))
        self.widget.setObjectName("widget")
        self.btn_msgSend = QtWidgets.QPushButton(self.page_chatting)
        self.btn_msgSend.setGeometry(QtCore.QRect(900, 740, 70, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.btn_msgSend.setFont(font)
        self.btn_msgSend.setObjectName("btn_msgSend")
        self.text_mas = QtWidgets.QTextEdit(self.page_chatting)
        self.text_mas.setGeometry(QtCore.QRect(5, 630, 990, 100))
        self.text_mas.setObjectName("text_mas")
        self.stackedWidget.addWidget(self.page_chatting)
        self.page_questionnaire = QtWidgets.QWidget()
        self.page_questionnaire.setObjectName("page_questionnaire")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_questionnaire)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 170, 56, 17))
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_questionnaire)
        self.page_ce = QtWidgets.QWidget()
        self.page_ce.setObjectName("page_ce")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_ce)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 150, 56, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_ce)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_setting)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 170, 56, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.stackedWidget.addWidget(self.page_setting)
        self.page_model = QtWidgets.QWidget()
        self.page_model.setObjectName("page_model")
        self.pushButton = QtWidgets.QPushButton(self.page_model)
        self.pushButton.setGeometry(QtCore.QRect(40, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_model)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_model)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 180, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.page_model)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menu_2.setFont(font)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menu_3.setFont(font)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menu_4.setFont(font)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.menu_5.setFont(font)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.text_msgBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_msgSend.setText(_translate("MainWindow", "发送"))
        self.pushButton_4.setText(_translate("MainWindow", "心理问卷"))
        self.pushButton_5.setText(_translate("MainWindow", "综合评价"))
        self.pushButton_6.setText(_translate("MainWindow", "设置"))
        self.pushButton.setText(_translate("MainWindow", "情绪词典"))
        self.pushButton_2.setText(_translate("MainWindow", "公开数据"))
        self.pushButton_3.setText(_translate("MainWindow", "深度学习训练"))
        self.menu.setTitle(_translate("MainWindow", "聊天区"))
        self.menu_2.setTitle(_translate("MainWindow", "情绪分类模型"))
        self.menu_3.setTitle(_translate("MainWindow", "心理问卷"))
        self.menu_4.setTitle(_translate("MainWindow", "综合评价"))
        self.menu_5.setTitle(_translate("MainWindow", "设置"))
