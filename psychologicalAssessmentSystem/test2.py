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
        self.delay_timer.timeout.connect(self.start_conversation)
        self.delay_timer.start(5000)  # 启动5秒的延迟

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

        # 获取AI的回复
        ai_response = self.get_ai_response()
        self.chat_history.append("AI: " + ai_response)

    def start_conversation(self):
        self.delay_timer.stop()
        self.send_welcome_message()  # 在应用启动后5秒发送欢迎消息

    def send_welcome_message(self):
        welcome_message = "Hello! I'm here to chat with you."  # 发送欢迎消息
        self.chat_history.append("AI: " + welcome_message)

    def get_ai_response(self):
        # 获取当前问题
        current_question = self.questions[self.current_question]
        self.current_question = (self.current_question + 1) % len(self.questions)  # 切换到下一个问题

        return current_question

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = SimpleChatBotApp()
    sys.exit(app.exec_())
