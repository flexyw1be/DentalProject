from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import get_without_failing
from data.config import *


class Schedule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(SCHEDULE_UI, self)
        self.setWindowTitle('Расписание')
        self.setWindowIcon(QIcon(ICON))
        self.set_history()

    def set_history(self):
        notes = get_without_failing(History, History.id)
        print(notes)
        for i in notes:
            patient = Patient.get(Patient.id == i.Patient_id)
            doctor = Doctor.get(Doctor.id == i.Doctor_id)
            self.list_widget.addItem(f'{i.datetime}    {patient.current_name}    {doctor.current_name}    {i.amount}    {i.name}    {i.note}')
