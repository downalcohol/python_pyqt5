# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_login(object):
    def setupUi(self, form_login):
        form_login.setObjectName("form_login")
        form_login.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(form_login)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 80, 241, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.login_form = QtWidgets.QGridLayout(self.layoutWidget)
        self.login_form.setContentsMargins(0, 0, 0, 0)
        self.login_form.setObjectName("login_form")
        self.line_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_password.setObjectName("line_password")
        self.login_form.addWidget(self.line_password, 2, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.login_form.addWidget(self.label_password, 2, 0, 1, 1)
        self.line_userName = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_userName.setObjectName("line_userName")
        self.login_form.addWidget(self.line_userName, 1, 1, 1, 1)
        self.label_userName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_userName.setFont(font)
        self.label_userName.setObjectName("label_userName")
        self.login_form.addWidget(self.label_userName, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(form_login)
        self.title.setEnabled(True)
        self.title.setGeometry(QtCore.QRect(0, 0, 400, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.btn_login = QtWidgets.QPushButton(form_login)
        self.btn_login.setGeometry(QtCore.QRect(160, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")

        self.retranslateUi(form_login)
        QtCore.QMetaObject.connectSlotsByName(form_login)

    def retranslateUi(self, form_login):
        _translate = QtCore.QCoreApplication.translate
        form_login.setWindowTitle(_translate("form_login", "Form"))
        self.label_password.setText(_translate("form_login", "密码"))
        self.label_userName.setText(_translate("form_login", "账号"))
        self.title.setText(_translate("form_login", "心理测评系统"))
        self.btn_login.setText(_translate("form_login", "登录"))