import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
# from chatbot import ChatBot  # chatbot是一个自定义的聊天机器人类

class LocalAIChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

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

        # self.chatbot = ChatBot()  # 创建聊天机器人实例

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Local AI Chat')
        self.show()

    def send_message(self):
        user_message = self.chat_input.text()
        self.chat_input.clear()

        # 显示用户消息
        self.chat_history.append("You: " + user_message)

        # 调用聊天机器人获取回复
        ai_response = self.chatbot.get_response(user_message)

        # 显示AI的回复
        self.chat_history.append("AI: " + ai_response)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = LocalAIChatApp()
    sys.exit(app.exec_())
