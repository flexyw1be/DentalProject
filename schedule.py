from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from MainWindow import *
from utitlities import get_without_failing
from config import *


class Schedule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/schedule.ui', self)
        self.setWindowTitle('RРасписание')
        self.setWindowIcon(QIcon(ICON))
