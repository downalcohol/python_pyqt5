import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import QTimer

class SimpleChatBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.questions = ["What is your favorite color?", "What's the weather like today?", "Do you have any plans for the weekend?"]
        self.current_question = 0
        self.delay_timer = QTimer(self)
        self.delay_timer.timeout.connect(self.ask_question)
        self.send_welcome_message()  # 在应用启动时发送欢迎消息

    def initUI(self):
        self.chat_history = QTextEdit(self)
        self.chat_input = QLineEdit(self)
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_history)
        layout.addWidget(self.chat_input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Simple Chat Bot')
        self.show()

    def send_message(self):
        user_message = self.chat_input.text()
        self.chat_input.clear()

        # 显示用户消息
        self.chat_history.append("You: " + user_message)

        self.handle_user_response(user_message)

    def send_welcome_message(self):
        greeting = "Hello! I'm here to chat with you."  # 发送问候语
        self.chat_history.append("AI: " + greeting)
        self.delay_timer.start(0)  # 立即开始提问

    def handle_user_response(self, user_response):
        if self.current_question == 0:
            self.delay_timer.start(5000)  # 设置5秒延迟，等待用户回复

    def ask_question(self):
        if self.current_question < len(self.questions):
            current_question = self.questions[self.current_question]
            self.chat_history.append("AI: " + current_question)
            self.current_question += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = SimpleChatBotApp()
    sys.exit(app.exec_())
