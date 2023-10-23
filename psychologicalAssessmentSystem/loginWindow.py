import sys

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

import loginForm
from mainWindow import MainWindow


# 创建main_window类继承my_main_window.py里面全部内容
class LoginWindow(loginForm.Ui_form_login, QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        # 连接登录按钮的点击事件到验证函数
        self.btn_login.clicked.connect(self.login)

    # 账号验证函数
    def login(self):
        # 获取用户名和密码
        username = self.line_userName.text()
        password = self.line_password.text()

        # 进行简单的用户名和密码验证
        if username == "111" and password == "111":
            # 登录成功
            QMessageBox.information(self, "登录成功", "欢迎登录！")

            # 创建并显示主窗口
            main_window.show()

            # 关闭登录窗口
            self.hide()
        else:
            QMessageBox.warning(self, "登录失败", "用户名或密码不正确")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 为main_window类和login_window类创建对象
    main_window = MainWindow()
    login_window = LoginWindow()
    # 显示登陆窗口
    login_window.show()

    sys.exit(app.exec_())
