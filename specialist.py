from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import *
from data.config import *


class Specialist(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi(SPECIALIST_UI, self)
        self.setWindowTitle('Пользователь')
        self.setWindowIcon(QIcon(ICON))
        self.name = name
        member = Doctor.get(Doctor.current_name == self.name)
        self.name_label.setText(f'{member.last_name} {member.first_name} {member.middle_name}')
        self.date_label.setText(member.date)
        self.number_label.setText(f'{member.number}')
        self.adress_label.setText(member.address)
        # self.date_label.setText(member.date)
        # self.address_label.setText(member.address)
        # self.number_label.setText(str(member.number))
