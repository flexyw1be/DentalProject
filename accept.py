from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import get_without_failing
from data.config import *


class Accept(QMainWindow):
    def __init__(self, text):
        super().__init__()
        uic.loadUi(ACCEPT_UI, self)
        self.setWindowTitle('Подтверждение')
        self.setWindowIcon(QIcon(ICON))
        self.label.setText(text)
        self.accept_push_button.clicked.connect(self.ok)
        self.not_accept_push_button.clicked.connect(self.not_ok)
        self.proof = ''

    def ok(self):
        self.proof = True
        self.hide()
        return self.proof

    def not_ok(self):
        self.proof = False
        self.hide()
        return self.proof
