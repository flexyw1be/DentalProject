from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import get_without_failing
from config import *


class Schedule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(SCHEDULE_UI, self)
        self.setWindowTitle('Расписание')
        self.setWindowIcon(QIcon(ICON))
