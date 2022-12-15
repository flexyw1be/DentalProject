from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from MainWindow import *
from utitlities import get_without_failing
from config import *


class MedicalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/medicalCard.ui', self)
        self.setWindowTitle('Медицинская Карта')
        self.setWindowIcon(QIcon(ICON))
