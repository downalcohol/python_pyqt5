import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QStackedLayout, \
    QLabel, QMainWindow


class Window1(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        QLabel("我是抽屉1要显示的内容", self)
        self.setStyleSheet("background-color:green;")


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2要显示的内容", self)
        self.setStyleSheet("background-color:red;")


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.creat_stacked_layout()
        self.init()

    def creat_stacked_layout(self):
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()

        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init(self):
        self.setFixedSize(800, 600)
        container = QVBoxLayout()

        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")

        btn1.clicked.connect(self.btn_press1_clicked)
        btn2.clicked.connect(self.btn_press2_clicked)

        container.addWidget(widget)
        container.addWidget(btn1)
        container.addWidget(btn2)

        self.setLayout(container)

    def btn_press1_clicked(self):
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
