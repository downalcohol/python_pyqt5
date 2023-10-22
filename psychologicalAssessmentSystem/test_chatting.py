import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextBrowser, QLineEdit

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat Application")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.chat_view = QTextBrowser()
        self.layout.addWidget(self.chat_view)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        self.layout.addWidget(send_button)

    def send_message(self):
        message = self.input_field.text()
        if message:
            self.chat_view.append(f"You: {message}")
            self.input_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
