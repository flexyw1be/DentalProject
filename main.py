from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from MainWindow import *
from utitlities import get_without_failing
from config import *


class Enter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/enter1.ui', self)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon(ICON))

        # подключаем кнопки
        self.admin_push_button.clicked.connect(self.set_admin_user)
        self.doctor_push_button.clicked.connect(self.set_doctor_user)
        self.enter_push_button.clicked.connect(self.enter)

        self.admin_push_button.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : lightgreen;"
                                             "}")

        # объявление переменных
        self.user_names = ADMINS
        self.set_usernames()

    def set_admin_user(self):
        self.admin_push_button.setStyleSheet("QPushButton"
                                             "{"
                                             "background-color : lightgreen;"
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
                                              "background-color : lightgreen;"
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
        self.main_window = MainWindow(self.users_combo_box.currentText())
        self.main_window.show()
        self.hide()

