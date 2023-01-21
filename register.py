from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from data.all_models import *
from data.config import *
import sys
from PyQt5.QtWidgets import QApplication
from utitlities import *


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

    def get_position(self):
        return self.position_combo_box.currentText()

    def register(self):
        model = DATABESES_KEYS[self.get_position()]
        if self.password_line_edit.text() and self.first_name_line_edit.text() and self.last_name_line_edit.text() \
                and self.middle_name_line_edit.text():
            current_name = f"{self.first_name_line_edit.text()} {self.last_name_line_edit.text()[0].upper()}. {self.middle_name_line_edit.text()[0].upper()}."
            model.create(last_name=self.last_name_line_edit.text(), first_name=self.first_name_line_edit.text(),
                         middle_name=self.middle_name_line_edit.text(), current_name=current_name,
                         password=self.password_line_edit.text())
        else:
            self.valid_label.setText('Заполните все поля')


#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ex = Register()
    sys.excepthook = except_hook
    main_ex.show()
    sys.exit(app.exec())
