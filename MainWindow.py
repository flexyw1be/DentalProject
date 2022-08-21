from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from config import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.firstTimeComboBox.addItems([f'{x}:00' for x in range(START_TIME, FINISH_TIME)])
        self.firstTimeComboBox.activated[str].connect(self.onActivated)


    def exit(self):
        pass

    def settings(self):
        pass

    def onActivated(self):
        n = int(self.firstTimeComboBox.currentText().split(':')[0])
        self.lastTimeComboBox.clear()
        self.lastTimeComboBox.addItems([f'{x}:00' for x in range(n, FINISH_TIME + 1)])
