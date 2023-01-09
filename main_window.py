import peewee
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from datetime import datetime
from data.all_models import *
from config import *
from medicalCard import MedicalCard
from schedule import Schedule
from specialist import Specialist
from utitlities import *


class MainWindow(QMainWindow):
    def __init__(self, name, permission):
        super().__init__()
        uic.loadUi(MAIN_UI, self)
        self.setWindowIcon(QIcon(ICON))
        self.user_name = name
        self.permission = permission
        if self.permission == DOCTORS:
            self.shedule_push_button.hide()
        print(self.user_name)
        if self.permission == DOCTORS:
            self.label_4.hide()
            self.doctor_combo_box.hide()
        self.setWindowTitle('Главная')
        self.firstTimeComboBox.addItems([f'{x}:00' for x in range(START_TIME, FINISH_TIME)])
        self.firstTimeComboBox.activated[str].connect(self.onActivated)
        self.tableWidget.cellClicked.connect(self.get_selected_cell_value)

        self.card_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "qproperty-icon: url(data/medicalCard.png);"

                                            "}")
        self.shedule_push_button.setStyleSheet("QPushButton"
                                               "{"
                                               "qproperty-icon: url(data/calendar.png);"

                                               "}")
        self.specialist_push_button.setStyleSheet("QPushButton"
                                                  "{"
                                                  "qproperty-icon: url(data/specialist.png);"

                                                  "}")
        self.specialist_push_button.setIconSize(QSize(55, 55))
        self.card_push_button.setIconSize(QSize(55, 55))
        self.shedule_push_button.setIconSize(QSize(55, 55))
        self.specialist_push_button.clicked.connect(self.show_specialist)
        self.card_push_button.clicked.connect(self.show_card)
        self.shedule_push_button.clicked.connect(self.show_schedule)
        self.name_label.setText(self.user_name)

        self.cancel_push_button.clicked.connect(self.set_canceled_appointments)
        self.ring_push_button.clicked.connect(self.set_ring_patients)

        self.ring_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : lightgrey;"
                                            "}")
        self.cancel_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : white;"
                                              "}"
                                              )

        self.table_sort = 'canceled_appointments'

    def exit(self):
        quit()

    def settings(self):
        pass

    def onActivated(self):
        n = int(self.firstTimeComboBox.currentText().split(':')[0])
        self.lastTimeComboBox.clear()
        self.lastTimeComboBox.addItems([f'{x}:00' for x in range(n, FINISH_TIME + 1)])

    def show_card(self):
        self.card = MedicalCard(self.get_selected_cell_value())
        self.card.show()

    def show_schedule(self):
        self.schedule = Schedule()
        self.schedule.show()

    def show_specialist(self):
        self.specialist = Specialist(self.user_name)
        self.specialist.show()

    def set_ring_patients(self):
        self.ring_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : lightgrey;"
                                            "}")
        self.cancel_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : white;"
                                              "}"
                                              )
        # self.ring_push_button.resize(176, 28)
        # self.cancel_push_button.resize(176, 28)
        self.table_sort = 'canceled_appointments'
        self.lose_push_button.show()
        self.accept_push_button.show()

    def set_canceled_appointments(self):
        self.ring_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : white;"
                                            "}")
        self.cancel_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : lightgrey;"
                                              "}"
                                              )

        # print(1)
        # self.ring_push_button.resize(176, 28)
        # self.cancel_push_button.resize(176, 28)
        self.table_sort = 'ring_patients'
        self.lose_push_button.hide()
        self.accept_push_button.hide()

    def set_patients_table(self):
        # Написать чтобы выбирала пациентов из основной таблицы
        pass

    def get_selected_cell_value(self):
        current_row = self.tableWidget.currentRow()
        current_column = 0
        return self.tableWidget.item(current_row, current_column).text()
