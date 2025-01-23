import main_window
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import *
from data.config import *
from accept import Accept
from error import Error
import datetime
from edit_medical_card import Edit

class MedicalCard(QMainWindow):
    def __init__(self, name, date, time, doctor):
        super().__init__()
        uic.loadUi(MEDICAL_CARD_UI, self)
        self.setWindowTitle('Медицинская Карта')
        self.setWindowIcon(QIcon(ICON))
        self.name = name
        self.doctor = doctor
        member = Patient.get(Patient.current_name == self.name)
        self.patient_name = f'{member.last_name} {member.first_name} {member.middle_name}'
        self.patient_date = member.date
        self.patient_address = member.address
        self.update_list_of_notes(member)
        self.patient_number = str(member.number)

        self.name_label.setText(self.patient_name)
        self.date_label.setText(self.patient_date)
        self.address_label.setText(member.address)
        self.number_label.setText(str(member.number))
        self.preparations = self.get_preparations()
        self.services = self.get_services()
        self.date = date
        self.time = time
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
        self.list_of_services = {}
        self.save_push_button.clicked.connect(self.check_note)
        self.editButton.clicked.connect(self.edit)

        self.accept_widget = Accept('')
        self.accept_widget.accept_push_button.clicked.connect(self.ok)
        self.accept_widget.not_accept_push_button.clicked.connect(self.not_ok)

        self.error_widget = Error('')
        self.error_widget.accept_push_button.clicked.connect(self.error)

        self.delete_push_button.clicked.connect(self.delete_service)

        s = get_without_failing(History, (History.datetime == f'{self.date} {self.time}'))
        print(s)
        if s:
            self.save_push_button.setText('Изменить')
            history_note = History.get(History.datetime == f'{self.date} {self.time}')
            self.cost = history_note.amount
            print(history_note.list_of_services)
            self.cost_line_edit.setText(str(history_note.amount))
            for i in history_note.list_of_services.split('\n'):
                name, count, price = i.split()
                name = name[:-1]
                if name not in self.list_of_services:
                    self.list_of_services[name] = [0, 0]
                self.list_of_services[name][0] += int(count)
                self.list_of_services[name][1] += int(price)
            self.update_price_list()
            self.appeal_text_edit.setPlainText(str(history_note.name))
            self.note_text_edit.setPlainText(str(history_note.note))

        self.get_prices()

    def get_history(self):
        pass

    def edit(self):
        self.card = Edit(self.patient_name, self.patient_date, self.patient_number,self.patient_address)
        self.card.show()

    def get_prices(self):
        self.list_of_amounts.clear()
        patient = Patient.get(Patient.current_name == self.name)
        notes = get_without_failing(History, History.Patient_id == patient.id)
        price = 0
        if not notes:
            return
        for i in notes:
            self.list_of_amounts.addItem(f'{i.datetime}      {i.amount}')
            price += i.amount
        self.amount_label.setText(str(price))

    def delete_service(self):
        name = self.price_list.currentItem().text().split()[0][:-1]
        count = self.list_of_services[name][0]
        price = self.list_of_services[name][1] // count
        self.list_of_services[name] = [count - 1, (count - 1) * price]
        self.cost -= price
        print(self.list_of_services)
        self.update_price_list()

    def add_service(self):
        if self.services_combo_box.currentText() in self.list_of_services:
            self.list_of_services[self.services_combo_box.currentText()][0] += self.count_spin_box.value()
        else:
            self.list_of_services[self.services_combo_box.currentText()] = [self.count_spin_box.value(), 0]
        print(self.services_combo_box.currentText())
        if self.serv:
            article = Services.get(Services.name == self.services_combo_box.currentText()).article
        else:
            article = Preparations.get(Preparations.name == self.services_combo_box.currentText()).article

        price = Price.get(Price.article == article).price
        self.list_of_services[self.services_combo_box.currentText()][1] = \
            self.list_of_services[self.services_combo_box.currentText()][0] * price
        self.cost += price * self.count_spin_box.value()
        self.update_price_list()
        self.count_spin_box.setValue(0)

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
        self.serv = True

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
        self.serv = False

    def get_preparations(self):
        prep = get_without_failing(Preparations, Preparations.id >= 0)
        list_of_names = [i.name for i in prep]
        return list_of_names

    def get_services(self):
        serv = get_without_failing(Services, Services.id >= 0)
        list_of_names = [i.name for i in serv]
        return list_of_names

    def update_price_list(self):
        self.price_list.clear()
        for i in self.list_of_services.keys():
            if self.list_of_services[i][0] > 0:
                self.price_list.addItem(
                    f'{str(i).capitalize()}: {self.list_of_services[i][0]}  {self.list_of_services[i][1]}')
        self.cost_line_edit.setText(str(self.cost))
        items = [self.price_list.item(x).text() for x in range(self.price_list.count())]
        print(items)

    def check_note(self):
        if len(self.appeal_text_edit.toPlainText()) == 0 or len(self.note_text_edit.toPlainText()) == 0:
            self.check(self.error_widget, self.pass_func, 'Проверьте правильность введенных данных')
            return
        self.check(self.accept_widget, self.save_note, 'Подтвердить введеную информацию')

    def save_note(self):
        member = Patient.get(Patient.current_name == self.name)
        print(self.doctor)
        doctor = Doctor.get(Doctor.current_name == self.doctor)
        print(self.date, self.time, member.id, doctor.id, ' '.join(self.list_of_services), self.cost,
              self.note_text_edit.toPlainText())
        s = get_without_failing(History, History.datetime == f'{self.date} {self.time}')
        items = [self.price_list.item(x).text() for x in range(self.price_list.count())]
        if not s:
            history_note = History.create(name=str(self.appeal_text_edit.toPlainText()),
                                          datetime=f'{self.date} {self.time}',
                                          Patient_id=member.id, Doctor_id=doctor.id, list_of_services='\n'.join(items),
                                          amount=self.cost, note=self.note_text_edit.toPlainText())
        else:
            self.save_push_button.setText('Изменить')
            history_note = History.get(History.datetime == f'{self.date} {self.time}')
            history_note.list_of_services = ' '.join(items)
            history_note.amount = self.cost
            history_note.note = self.note_text_edit.toPlainText()
            history_note.save()
            self.update_list_of_notes(member)
        self.get_prices()

    def check(self, main_func, func, text):
        main_func.accept_push_button.clicked.connect(func)
        main_func.label.setText(text)
        main_func.show()
        self.setEnabled(False)

    def ok(self):
        self.accept_widget.hide()
        self.setEnabled(True)

    def not_ok(self):
        self.accept_widget.hide()
        self.setEnabled(True)

    def pass_func(self):
        return

    def error(self):
        self.error_widget.hide()
        self.setEnabled(True)

    def update_list_of_notes(self, member):
        s = get_without_failing(History, History.Patient_id == member.id)
        if s:
            for n, i in enumerate(s):
                doctor = Doctor.get(Doctor.id == i.Doctor_id)
                self.list_of_notes.addItem(
                    f'{n + 1}    |   {doctor.current_name}   |   {i.datetime}    |   {i.name}    |   {i.note}')
