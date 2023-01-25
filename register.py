import sys
import hashlib

from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from utitlities import *
from error import *
from data.all_models import *
from data.config import *


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(REGISTER_UI, self)
        self.setWindowTitle('Register')
        self.setWindowIcon(QIcon(ICON))

        # подсказки полей ввода и шифрование пароля
        self.password_line_edit.setPlaceholderText('Введите пароль')
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.last_name_line_edit.setPlaceholderText('Введите имя')
        self.first_name_line_edit.setPlaceholderText('Введите фамилию')
        self.middle_name_line_edit.setPlaceholderText('Введите отчетство')

        # подключение кнопок к методам класса
        self.register_push_button.clicked.connect(self.register)

        self.check_widget = Error('Успешно')
        self.check_widget.accept_push_button.clicked.connect(self.ok)

    def get_position(self):
        return self.position_combo_box.currentText()

    def register(self):
        model = DATABESES_KEYS[self.get_position()]
        if self.password_line_edit.text() and self.first_name_line_edit.text() and self.last_name_line_edit.text() \
                and self.middle_name_line_edit.text():
            current_name = f"{self.first_name_line_edit.text()} {self.last_name_line_edit.text()[0].upper()}. {self.middle_name_line_edit.text()[0].upper()}."
            model.create(last_name=self.last_name_line_edit.text(), first_name=self.first_name_line_edit.text(),
                         middle_name=self.middle_name_line_edit.text(), current_name=current_name,
                         password=self.hasher(self.password_line_edit.text()))
            self.check_widget.show()
        else:
            self.valid_label.setText('Заполните все поля')

    def ok(self):
        self.check_widget.hide()

    def hasher(self, password):
        salt = '123'.encode('utf-8')
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000)
        return key


#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ex = Register()
    sys.excepthook = except_hook
    main_ex.show()
    sys.exit(app.exec())
