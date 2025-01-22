from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon

import hashlib
from data.all_models import *
from main_window import MainWindow
from PyQt5 import uic
from utitlities import *
from data.config import *


class Enter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ENTER_UI, self)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon(ICON))

        # подключаем кнопки
        self.admin_push_button.clicked.connect(self.set_admin_user)
        self.doctor_push_button.clicked.connect(self.set_doctor_user)
        self.enter_push_button.clicked.connect(self.enter)
        self.exit_push_button.clicked.connect(self.exit)
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.exit_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "background-color : lightgrey;"
                                            "}")

        self.admin_push_button.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : lightgrey;"
                                             "}")
        self.doctor_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : white;"
                                              "}")

        # объявление переменных
        self.user_names = ADMINS
        self.set_usernames()

    def set_admin_user(self):
        self.admin_push_button.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : lightgrey;"
                                             "}")
        self.doctor_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : white;"
                                              "}")
        self.user_names = ADMINS
        self.set_usernames()

    def set_doctor_user(self):
        self.doctor_push_button.setStyleSheet("QPushButton"
                                              "{"
                                              "background-color : lightgrey;"
                                              "}")
        self.admin_push_button.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : white;"
                                             "}"
                                             )
        self.user_names = DOCTORS
        self.set_usernames()

    def set_usernames(self):
        self.users_combo_box.clear()
        self.users_combo_box.addItems(self.user_names)

    def enter(self):
        if self.check_password():
            self.main_window = MainWindow(self.users_combo_box.currentText(), self.user_names)
            self.main_window.show()
            self.hide()
        else:
            self.password_label.setText('Пароль не подходит')

    def check_password(self):
        name = self.users_combo_box.currentText()
        if self.user_names == ADMINS:
            member = Admin.get(Admin.current_name == name)
        else:
            member = Doctor.get(Doctor.current_name == name)
        salt = '123'.encode('utf-8')
        key = hashlib.pbkdf2_hmac(
            'sha256',
            self.password_line_edit.text().encode('utf-8'),
            salt,
            100000)
        return member.password == key

    def exit(self):
        quit()
