import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    #设置窗口标题
    w.setWindowTitle(' 第一个PyQt')

    #在窗口里面添加控件
    btn = QPushButton('按钮')

    #设置按钮的父对象
    btn.setParent(w)

    label = QLabel("账号",w)

    # 设置图表
    w.setWindowIcon(QIcon("hollow.jpg"))

    #展示窗口
    # w.setGeometry(20,20,30,30)
    # w.resize(800,600)
    # 设置窗口在屏幕正中   
    screen = QDesktopWidget().screenGeometry()
    window = w.geometry()
    x = (screen.width() - window.width()) //2
    y = (screen.height() - window.height()) //2
    w.move(x,y)
    w.resize(800,600)
    w.show()

    #程序进行循环等待状态
    app.exec_()