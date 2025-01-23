import peewee
import openpyxl
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QIcon
from datetime import datetime, time, date, timedelta
from data.all_models import *
from data.config import *
from medicalCard import MedicalCard
from schedule import Schedule
from specialist import Specialist
from utitlities import *
from accept import Accept
from error import Error


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
            self.doctor_combo_box.hide()
        self.setWindowTitle('Главная')
        self.table_widget.cellClicked.connect(self.get_selected_cell_value)

        doctors = [i.current_name for i in get_without_failing(Doctor, (Doctor.id > 0))]
        self.doctor_combo_box.addItems(doctors)
        print(self.doctor_combo_box.currentText())
        self.proof = False
        # self.get_xlsx()
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
        self.last_name_line_edit.SelectedText = 'привет'
        self.shedule_push_button.clicked.connect(self.show_schedule)
        self.name_label.setText(self.user_name)

        self.cancel_notes_push_button.clicked.connect(self.set_canceled_appointments)
        self.ring_push_button.clicked.connect(self.set_ring_patients)

        self.ring_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : lightgrey;"
                                            "}")
        self.cancel_notes_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : white;"
                                                    "}"
                                                    )

        self.table_sort = 'canceled_appointments'

        self.add_note_push_button.clicked.connect(self.add_note)

        self.calendar_widget.clicked.connect(self.show_notes)

        self.cancel_push_button.clicked.connect(self.delete_note)

        self.lose_push_button.clicked.connect(self.cancel_note)
        self.get_ring_patients()

        self.show_notes()
        self.accept_widget = Accept('')
        self.accept_widget.accept_push_button.clicked.connect(self.ok)
        self.accept_widget.not_accept_push_button.clicked.connect(self.not_ok)

        self.error_widget = Error('')
        self.error_widget.accept_push_button.clicked.connect(self.error)

    def exit(self):
        quit()

    def settings(self):
        pass

    def onActivated(self):
        n = int(self.firstTimeComboBox.currentText().split(':')[0])
        self.lastTimeComboBox.clear()
        self.lastTimeComboBox.addItems([f'{x}:00' for x in range(n, FINISH_TIME + 1)])

    def show_card(self):
        value = self.get_selected_cell_value()
        if not value:
            return
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2]).strftime('%d-%m-%y')
        print(value[2])
        self.card = MedicalCard(value[1], date, value[0], value[2])
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
        self.cancel_notes_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : white;"
                                                    "}"
                                                    )

        self.table_sort = 'canceled_appointments'
        self.lose_push_button.show()
        self.accept_push_button.show()
        self.get_ring_patients()

    def get_ring_patients(self):
        date = datetime.today().date()
        s = get_without_failing(Note, Note.date == date.strftime('%d-%m-%y'))
        self.patients_table.clear()
        if not s:
            return
        for i in s:
            if i.status != False:
                patient = Patient.get(Patient.id == i.Patient_id)
                self.patients_table.addItem(f'{patient.current_name}    : {patient.number}')

    def get_canceled_patients(self):
        date = datetime.today().date()
        s = get_without_failing(Note, Note.date == date.strftime('%d-%m-%y'))
        self.patients_table.clear()
        if not s:
            return
        for i in s:
            if i.status == False:
                patient = Patient.get(Patient.id == i.Patient_id)
                self.patients_table.addItem(f'{patient.current_name}    : {patient.number}')

    def cancel_note(self):
        name = self.patients_table.currentItem()
        if not name:
            return
        name = name.text().split('    : ')[0]
        print(name)
        patient = Patient.get(Patient.current_name == name)
        date = datetime.today().date()
        date1 = date - timedelta(days=1)
        s = get_without_failing(Note, date1 < Note.date <= date and Note.Patient_id == patient.id)
        for i in s:
            i.status = False
            i.save()
        self.get_ring_patients()

    def set_canceled_appointments(self):
        self.ring_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : white;"
                                            "}")
        self.cancel_notes_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : lightgrey;"
                                                    "}"
                                                    )

        self.table_sort = 'ring_patients'
        self.lose_push_button.hide()
        self.accept_push_button.hide()
        self.patients_table.clear()
        self.get_canceled_patients()

    def get_selected_cell_value(self):
        current_row = self.table_widget.currentRow()
        current_column = 0
        if not self.table_widget.item(current_row, current_column) or not self.table_widget.item(current_row, 1):
            self.check(self.error_widget, self.pass_func, 'Ошибка\nВыберите запись')
            return 0
        return self.table_widget.item(current_row, current_column).text(), self.table_widget.item(current_row,
                                                                                                  1).text(), self.table_widget.item(
            current_row, 2).text()

    def get_row(self):
        return self.table_widget.currentRow()

    def add_note(self):
        self.check(self.accept_widget, self.set_note, 'Подтвердите запись')

    def set_note(self):
        current_name = f"{self.last_name_line_edit.text()} {self.first_name_line_edit.text()[0].upper()}. {self.middle_name_line_edit.text()[0].upper()}."
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2]).date().strftime('%d-%m-%y')
        number = self.number_line_edit.text()
        doctor = Doctor.get(Doctor.current_name == self.doctor_combo_box.currentText())
        print(current_name)

        start_time = time(*list(map(int, self.start_time_edit.text().split(':'))))
        finish_time = time(*list(map(int, self.finish_time_edit.text().split(':'))))

        request = get_without_failing(Patient, Patient.current_name == current_name)
        print(request)
        if not request:
            member = Patient.create(last_name=self.last_name_line_edit.text(),
                                    first_name=self.first_name_line_edit.text(),
                                    middle_name=self.middle_name_line_edit.text(), current_name=current_name,
                                    start_time=start_time, finish_time=finish_time, number=number)
            member.save()
        member = Patient.get(Patient.current_name == current_name)
        note = Note.create(Patient_id=member.id, Doctor_id=doctor.id, date=date, start_time=start_time,
                           finish_time=finish_time)
        note.save()
        self.last_name_line_edit.setText('')
        self.first_name_line_edit.setText('')
        self.middle_name_line_edit.setText('')

        self.show_notes()

    def show_notes(self):
        list_of_notes = self.get_notes()

        self.table_widget.setRowCount(len(list_of_notes))
        # self.get_time()
        for n, i in enumerate(list_of_notes):
            print(i)
            self.table_widget.setItem(n, 0, QTableWidgetItem(i['Время']))
            self.table_widget.setItem(n, 1, QTableWidgetItem(i['Пациент']))
            self.table_widget.setItem(n, 2, QTableWidgetItem(i['Врач']))

    def get_notes(self):
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2]).date().strftime('%d-%m-%y')
        notes = get_without_failing(Note, (Note.date == date))
        list_of_notes = []
        if notes:
            for i in notes:
                member = Patient.get(Patient.id == i.Patient_id)
                doctor = Doctor.get(Doctor.id == i.Doctor_id)
                list_of_notes.append(
                    {'Дата': date, 'Время': i.start_time.strftime('%H:%M'),
                     'Пациент': member.current_name, 'Врач': doctor.current_name,
                     'Время окончания': i.finish_time.strftime('%H:%M'), })
        list_of_notes.sort(key=lambda x: int(x['Время'].split(':')[0]))
        return list_of_notes

    def delete_note(self):
        row = self.get_row()
        value = self.get_selected_cell_value()
        name = value[1]
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2]).date().strftime('%d-%m-%y')
        patient = Patient.get(Patient.current_name == name)
        print(date, name)

        note = Note.delete().where(Note.date == date, Note.Patient_id == patient.id)
        print(note, 14234)
        note.execute()

        self.table_widget.removeRow(row)
        # self.show_notes()

    def check(self, main_func, func, text):
        main_func.accept_push_button.clicked.connect(func)
        main_func.label.setText(text)
        main_func.show()
        self.setEnabled(False)

    def error(self):
        self.error_widget.hide()
        self.setEnabled(True)

    def ok(self):
        self.accept_widget.hide()
        self.setEnabled(True)

    def not_ok(self):
        self.accept_widget.hide()
        self.setEnabled(True)

    def pass_func(self):
        return

    def get_xlsx(self):
        wb = openpyxl.Workbook()
        list = wb.active
        list.append(('Дата', 'Время', 'Пациент', 'Врач', 'Причина обращения', 'Цена', 'Примечание'))
        notes = get_without_failing(History, History.id)
        for i in notes:
            patient = Patient.get(Patient.id == i.Patient_id)
            doctor = Doctor.get(Doctor.id == i.Doctor_id)
            list.append((
                i.datetime.split()[0], i.datetime.split()[1], patient.current_name, doctor.current_name, i.name,
                i.amount, i.note))
        wb.save('history.xlsx')
