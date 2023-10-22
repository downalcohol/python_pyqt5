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
        self.setWindowTitle("水平布局")

        layout = QHBoxLayout()

        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn3 = QPushButton("按钮3")

        # 添加一个伸缩器
        layout.addStretch(2)

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)

        layout.addStretch(2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget子类
    w = Mywindow()
    w.show()

    app.exec_()
