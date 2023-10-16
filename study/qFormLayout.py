import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QFormLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):

        container = QFormLayout()

        edit1 = QLineEdit()
        edit1.setPlaceholderText("请输入账号")
        container.addRow("账号：",edit1)

        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        container.addRow("密码：",edit2)

        self.setLayout(container)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()