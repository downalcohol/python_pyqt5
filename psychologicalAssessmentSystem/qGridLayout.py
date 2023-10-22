import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):

        data = {
            0:["7","8","9","+","("],
            1:["4","5","6","-",")"],
            2:["1","2","3","*","<-"],
            3:["0",",","=","/","C"]
        }
        container = QVBoxLayout()

        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")

        layout2 = QGridLayout()
        for lineNumber,line_data in data.items():
            for columnNumber,number in enumerate(line_data):
                btn = QPushButton(number)
                layout2.addWidget(btn,lineNumber,columnNumber)

        container.addWidget(edit)
        container.addLayout(layout2)

        self.setLayout(container)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()