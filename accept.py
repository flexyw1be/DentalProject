from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic, QtCore
from utitlities import get_without_failing
from data.config import *


class Accept(QMainWindow):
    def __init__(self, text):
        super().__init__()
        uic.loadUi(ACCEPT_UI, self)
        self.setWindowTitle('Подтверждение')
        self.setWindowIcon(QIcon(ICON))
        self.label.setText(text)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.widget_proof = False




