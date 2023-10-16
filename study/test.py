import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

if __name__ == '__main__':
    # application 对象
    app = QApplication(sys.argv)

    # QMainWindow对象
    ui = uic.loadUi("./untitled.ui")

    # 显示
    ui.show()

    sys.exit(app.exec_())
