from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import *
from config import *


class Specialist(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(SPECIALIST_UI, self)
        self.setWindowTitle('Пользователь')
        self.setWindowIcon(QIcon(ICON))
