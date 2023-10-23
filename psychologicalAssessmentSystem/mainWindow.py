import random
import time

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QTextDocument, QTextCursor, QTextFrameFormat, QTextBlockFormat
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QLineEdit

import mainForm


# 创建main_window类继承mainForm.py里面全部内容
class MainWindow(mainForm.Ui_MainWindow, QMainWindow):
    aiName = '小爱'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # 绑定菜单按钮切换页面

        self.findChild(QAction, "actionChatting").triggered.connect(self.switchToChatting)
        self.findChild(QAction, "actionModel").triggered.connect(self.switchToModel)
        self.findChild(QAction, "actionQuestionnaire").triggered.connect(self.switchToQuestionnaire)
        self.findChild(QAction, "actionCE").triggered.connect(self.switchToCE)
        self.findChild(QAction, "actionSetting").triggered.connect(self.switchToSetting)

        # 初始化聊天区界面
        # 设置机器人问题列表以及相关参数
        self.questions = ["What is your favorite color?", "What's the weather like today?",
                          "Do you have any plans for the weekend?"]
        random.shuffle(self.questions)  # 打乱问题列表的顺序
        self.current_question = 0
        self.delay_timer = QTimer(self)
        self.delay_timer.timeout.connect(self.start_conversation)
        self.delay_timer.start(4000)

        # 为消息发送按钮绑定事件
        self.btn_msgSend.clicked.connect(self.sendMsg)

    def switchToChatting(self):
        self.stackedWidget.setCurrentIndex(0)

    def switchToModel(self):
        self.stackedWidget.setCurrentIndex(1)

    def switchToQuestionnaire(self):
        self.stackedWidget.setCurrentIndex(2)

    def switchToCE(self):
        self.stackedWidget.setCurrentIndex(3)

    def switchToSetting(self):
        self.stackedWidget.setCurrentIndex(4)

    def sendMsg(self):
        user_message = self.line_msg.toPlainText()
        self.line_msg.clear()

        # 显示用户消息
        self.text_msgBrowser.setAlignment(Qt.AlignRight)
        self.text_msgBrowser.insertPlainText(user_message + "\n")

        # 获取AI的回复
        self.get_ai_response()

    def start_conversation(self):
        self.delay_timer.stop()
        self.send_welcome_message()  # 在应用启动后发送欢迎消息
        self.get_ai_response()

    def send_welcome_message(self):
        welcome_message = "Hello! I'm here to chat with you.\n\n"  # 发送欢迎消息
        self.text_msgBrowser.append(self.aiName + "：" + welcome_message)

    def get_ai_response(self):
        if self.current_question > len(self.questions): return
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.current_question += 1
            QTimer.singleShot(1000, lambda: self.show_ai_response(question))
        else:
            self.current_question += 1
            QTimer.singleShot(0, lambda: self.show_ai_response("Thank you for answering all the questions!"))

    def show_ai_response(self, ai_response):
        self.text_msgBrowser.setAlignment(Qt.AlignLeft)
        self.text_msgBrowser.insertPlainText(self.aiName + "：" + ai_response + "\n\n")
