import sys

from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QIcon
from data.all_models import *

isMain = False


def get_without_failing(Model, query):
    results = Model.select().where(query).limit(1)
    print(results)
    return results[0] if len(results) > 0 else None


class EnterWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/start.ui', self)
        self.setWindowTitle('Sign in')
        self.setWindowIcon(QIcon('data/deltadent1.png'))
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.pushButton.clicked.connect(self.enter)

    def enter(self):
        global isMain
        a = self.loginLineEdit.text()
        s = get_without_failing(LoginData, (LoginData.login == a))
        print(s.password, self.passwordLineEdit.text())
        print(s, s.password == self.passwordLineEdit.text())
        if s and s.password == self.passwordLineEdit.text():
            print('Вход выполнен')
            self.close()
            isMain = True


class RegisterWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/start.ui', self)
        self.setWindowTitle('Sign up')
        self.setWindowIcon(QIcon('data/deltadent1.png'))
        self.pushButton.clicked.connect(self.register)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        if isMain:
            self.hide()
            self.s = MainWidget()
            self.s.show()

    def register(self):
        print(1)
        LoginData.create(login=self.loginLineEdit.text(), password=self.passwordLineEdit.text())


class StartWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/enter.ui', self)
        self.setWindowTitle('Enter')
        self.setWindowIcon(QIcon('data/deltadent1.png'))
        self.signInPb.clicked.connect(self.enter)
        self.signUpPb.clicked.connect(self.register)

    def enter(self):
        self.s = EnterWidget()
        self.s.show()
        print(6)
        if isMain:
            self.close()
        print(isMain)

    def register(self):
        self.s = RegisterWidget()
        self.s.show()


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.setWindowTitle('Enter')
        self.setWindowIcon(QIcon('data/deltadent1.png'))
