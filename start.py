import sys

from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QIcon


class StartWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('enter.ui', self)
        self.setWindowTitle('Вход')
        self.setWindowIcon(QIcon('deltadent1.png'))
        # self.enterPushbutton.clicked.connect(self.enter)

    def enter(self):
        pass

    def register(self):
        pass


