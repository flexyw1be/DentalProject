import sys

from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QIcon
from data.all_models import *


class EnterWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.setWindowTitle('Вход')
        self.setWindowIcon(QIcon('deltadent1.png'))

    def f(self):
        pass


class RegisterWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.setWindowTitle('Вход')
        self.setWindowIcon(QIcon('deltadent1.png'))
        self.pushButton.clicked.connect(self.register)

    def register(self):
        print(1)
        LoginData.create(login=self.loginLineEdit.text(), password=self.passwordLineEdit.text())
        print(1)


class StartWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('enter.ui', self)
        self.setWindowTitle('Вход')
        self.setWindowIcon(QIcon('deltadent1.png'))
        self.signInPb.clicked.connect(self.enter)
        self.signUpPb.clicked.connect(self.register)

    def enter(self):
        self.s = EnterWidget()
        self.s.show()

    def register(self):
        self.s = RegisterWidget()
        print(1)
        self.s.show()
