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
        self.preparations = self.get_preparations()
        self.services = self.get_services()
        self.serv = True

        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : lightgrey;"
                                                "}")

        self.preparations_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : white;"
                                                    "}"
                                                    )
        self.set_services()
        self.services_push_button.clicked.connect(self.set_services)
        self.preparations_push_button.clicked.connect(self.set_preparations)
        self.add_push_button.clicked.connect(self.add_service)
        self.cost = 0

    def get_history(self):
        pass

    def get_prices(self):
        pass

    def add_service(self):
        self.price_list.addItem(f'{self.services_combo_box.currentText()}: {self.count_spin_box.value()}')
        print(self.services_combo_box.currentText())
        if self.serv:
            article = Services.get(Services.name == self.services_combo_box.currentText()).article
        else:
            article = Preparations.get(Preparations.name == self.services_combo_box.currentText()).article
        price = Price.get(Price.article == article).price
        self.cost += price * self.count_spin_box.value()
        self.count_spin_box.setValue(0)
        print(self.cost)

    def set_services(self):
        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : lightgrey;"
                                                "}")

        self.preparations_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : white;"
                                                    "}"
                                                    )
        self.services_combo_box.clear()
        self.services_combo_box.addItems(self.services)

    def set_preparations(self):
        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : white;"
                                                "}"
                                                )

        self.preparations_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : lightgrey;"
                                                    "}")
        self.services_combo_box.clear()
        self.services_combo_box.addItems(self.preparations)

    def get_preparations(self):
        prep = get_without_failing(Preparations, Preparations.id >= 0)
        list_of_names = [i.name for i in prep]
        return list_of_names

    def get_services(self):
        serv = get_without_failing(Services, Services.id >= 0)
        list_of_names = [i.name for i in serv]
        return list_of_names

    # def set_canceled_appointments(self):
    #     self.ring_push_button.setStyleSheet("QPushButton"
    #                                         "{"
    #                                         "background-color : white;"
    #                                         "}")
    #     self.cancel_notes_push_button.setStyleSheet("QPushButton"
    #                                                 "{"
    #                                                 "background-color : lightgrey;"
    #                                                 "}"
    #                                                 )
    #
    #     self.table_sort = 'ring_patients'
    #     self.lose_push_button.hide()
    #     self.accept_push_button.hide()
