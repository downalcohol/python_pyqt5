import random
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QFormLayout


class MyWindow(QWidget):
    clicked_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        container = QFormLayout()

        btn = QPushButton("点击")
        btn.clicked.connect(self.check)
        self.clicked_signal.connect(self.btn_clicked)

        container.addWidget(btn)

        self.setLayout(container)

    def btn_clicked(self,msg):
        print("test" + msg)

    def check(self):
        num = random.randint(1, 10)
        self.clicked_signal.emit(str(num))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
