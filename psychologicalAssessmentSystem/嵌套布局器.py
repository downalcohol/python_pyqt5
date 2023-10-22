import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Mywindow(QWidget):
    # 一定要调用父类的init方法 里面包含了很多对ui空间的初始化操作
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.resize(800, 600)
        self.setWindowTitle("嵌套布局")

        container = QVBoxLayout()

        hobby_box = QGroupBox("爱好")

        layout1 = QVBoxLayout()

        btn1 = QPushButton("唱")
        btn2 = QPushButton("跳")
        btn3 = QPushButton("rap")


        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout1.addWidget(btn3)

        hobby_box.setLayout(layout1)

        gender_box = QGroupBox("性别")

        layout2 = QHBoxLayout()

        btn4 = QPushButton("男")
        btn5 = QPushButton("女")
        btn6 = QPushButton("坤")

        layout2.addWidget(btn4)
        layout2.addWidget(btn5)
        layout2.addWidget(btn6)

        gender_box.setLayout(layout2)

        #将爱好空间和性别空间添加到容器中
        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget子类
    w = Mywindow()
    w.show()

    app.exec_()
