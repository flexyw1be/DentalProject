from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        # self.calendarWidget.clicked['QDate'].connect(self.show_date_func)

    def exit(self):
        pass

    def settings(self):
        pass
