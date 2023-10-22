import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# 导入login_window.py、my_main_window.py里面全部内容
import login
import main


# 创建main_window类继承my_main_window.py里面全部内容
class main_window(main.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)


class login_window(login.Ui_form_login, QMainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 为main_window类和login_window类创建对象
    main_window = main_window()
    login_window = login_window()
    # 显示登陆窗口
    login_window.show()

    # 定义一个槽函数，处理登录按钮的点击事件
    def handle_login():
        login_window.close()  # 关闭登录窗口
        main_window.show()  # 显示主窗口

    # 将槽函数与登录按钮的点击事件关联
    login_window.btn_login.clicked.connect(handle_login)

    # 关闭程序，释放资源
    sys.exit(app.exec_())