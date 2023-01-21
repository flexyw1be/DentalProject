from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import *
from data.config import *


class MedicalCard(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi(MEDICAL_CARD_UI, self)
        self.setWindowTitle('Медицинская Карта')
        self.setWindowIcon(QIcon(ICON))
        self.name = name

        member = Patient.get(Patient.current_name == self.name)
        self.name_label.setText(f'{member.last_name} {member.first_name} {member.middle_name}')
        self.date_label.setText(member.date)
        self.address_label.setText(member.address)
        self.number_label.setText(str(member.number))
