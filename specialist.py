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
        print(self.name)
        self.permission = 'doctor'
        member = get_without_failing(Doctor, Doctor.current_name == self.name)
        if not member:
            member = get_without_failing(Admin, Admin.current_name == self.name)
            self.permission = 'admin'
        member = member[0]
        self.name_label.setText(f'{member.first_name} {member.last_name} {member.middle_name}')
        if self.permission == 'doctor':
            self.date_label.setText(member.date) if member.date else ''
            self.number_label.setText(f'{member.number}') if member.number else ''
            self.adress_label.setText(member.address) if member.address else ''

