from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic, QtCore
from utitlities import get_without_failing
from data.config import *


class Edit(QMainWindow):
    def __init__(self, name, date, number, address):
        super().__init__()
        uic.loadUi(EDIT_MEDICAL_CARD_UI, self)
        self.setWindowTitle('Изменение')
        self.setWindowIcon(QIcon(ICON))
        self.widget_proof = False
        self.saveButton.clicked.connect(self.save)
        self.lineEdit1.setText(name)
        self.lineEdit2.setText(date)
        self.lineEdit3.setText(number)
        self.lineEdit4.setText(address)

    def save(self):
        self.hide()
