import peewee
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtGui import QIcon
from datetime import datetime, time
from data.all_models import *
from data.config import *
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
        self.table_widget.cellClicked.connect(self.get_selected_cell_value)

        doctors = [i.current_name for i in get_without_failing(Doctor, (Doctor.id > 0))]
        self.doctor_combo_box.addItems(doctors)
        print(self.doctor_combo_box.currentText())

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

        self.add_note_push_button.clicked.connect(self.add_note)

        self.calendar_widget.clicked.connect(self.show_notes)

        self.cancel_push_button.clicked.connect(self.delete_note)

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

        self.table_sort = 'ring_patients'
        self.lose_push_button.hide()
        self.accept_push_button.hide()

    def get_selected_cell_value(self):
        current_row = self.table_widget.currentRow()
        current_column = 0
        return self.table_widget.item(current_row, current_column).text(), self.table_widget.item(current_row, 2).text()

    def get_row(self):
        return self.table_widget.currentRow()

    def add_note(self):
        current_name = f"{self.first_name_line_edit.text()} {self.last_name_line_edit.text()[0].upper()}. {self.middle_name_line_edit.text()[0].upper()}."
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2])
        doctor = Doctor.get(Doctor.current_name == self.doctor_combo_box.currentText())

        start_time = time(*list(map(int, self.start_time_edit.text().split(':'))))
        finish_time = time(*list(map(int, self.finish_time_edit.text().split(':'))))

        if Patient.table_exists():
            member = Patient.create(last_name=self.last_name_line_edit.text(),
                                    first_name=self.first_name_line_edit.text(),
                                    middle_name=self.middle_name_line_edit.text(), current_name=current_name)
            member.save()
            note = Note.create(Patient_id=member.id, Doctor_id=doctor.id, date=date, start_time=start_time,
                               finish_time=finish_time)
            note.save()

        else:
            request = get_without_failing(Patient, (Patient.current_name == current_name))
            if not request:
                member = Patient.create(last_name=self.last_name_line_edit.text(),
                                        first_name=self.first_name_line_edit.text(),
                                        middle_name=self.middle_name_line_edit.text(), current_name=current_name,
                                        date=date, start_time=start_time, finish_time=finish_time)
                member.save()
                note = Note.create(Patient_id=member.id, Doctor_id=doctor.id, date=date, start_time=start_time,
                                   finish_time=finish_time)
                note.save()

    def show_notes(self):
        list_of_notes = self.get_notes()
        self.table_widget.setRowCount(len(list_of_notes))
        if list_of_notes:
            # start_time = list(map(int, list_of_notes[-1]['Время окончания'].split(":")))
            start_time = time(*list(map(int, list_of_notes[-1]['Время окончания'].split(":"))))
            self.start_time_edit.setMinimumTime(start_time)
            self.finish_time_edit.setMinimumTime(start_time)
        else:
            self.start_time_edit.setMinimumTime(time(8, 0))
            self.finish_time_edit.setMinimumTime(time(8, 0))
        for n, i in enumerate(list_of_notes):
            print(i)
            self.table_widget.setItem(n, 0, QTableWidgetItem(i['Дата']))
            self.table_widget.setItem(n, 1, QTableWidgetItem(i['Время']))
            self.table_widget.setItem(n, 2, QTableWidgetItem(i['Пациент']))
            self.table_widget.setItem(n, 3, QTableWidgetItem(i['Врач']))

    def get_notes(self):
        date = list(map(int, self.calendar_widget.selectedDate().toString('dd.MM.yyyy').split('.')))
        date = datetime(day=date[0], month=date[1], year=date[2])
        notes = get_without_failing(Note, (Note.date == date))
        list_of_notes = []
        if notes:
            for i in notes:
                member = Patient.get(Patient.id == i.Patient_id)
                doctor = Doctor.get(Doctor.id == i.Doctor_id)
                list_of_notes.append(
                    {'Дата': date.strftime('%d:%m:%y'), 'Время': i.start_time.strftime('%H:%M'),
                     'Пациент': member.current_name, 'Врач': doctor.current_name,
                     'Время окончания': i.finish_time.strftime('%H:%M'), })
        list_of_notes.sort(key=lambda x: x['Дата'])
        return list_of_notes

    def delete_note(self):
        row = self.get_row()
        date, name = self.get_selected_cell_value()
        print(date, name)
        patient = Patient.get(Patient.current_name==name)
        note = Note.delete().where(Note.date == date and Note.Patient_id == patient.id)
        note.execute()
        # self.table_widget.removeRow(row)
        self.show_notes()
        print(1)
