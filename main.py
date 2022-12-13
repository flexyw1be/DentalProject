from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from MainWindow import *
from utitlities import get_without_failing


# class Login(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('ui/start.ui', self)
#         self.setWindowTitle('Login')
#         self.setWindowIcon(QIcon(ICON))
#         self.loginButton.setEnabled(False)
#         self.loginLineEdit.setPlaceholderText('Please enter your login')
#         self.passwordLineEdit.setPlaceholderText('Please enter your password')
#         self.passwordLineEdit.setEchoMode(QLineEdit.Password)
#
#         self.loginLineEdit.textChanged.connect(self.check_input)
#         self.passwordLineEdit.textChanged.connect(self.check_input)
#
#         self.loginButton.clicked.connect(self.enter)
#         self.registerButton.clicked.connect(self.register)
#
#     def check_input(self):
#         if self.loginLineEdit.text() and self.passwordLineEdit.text():
#             self.loginButton.setEnabled(True)
#         else:
#             self.loginButton.setEnabled(False)
#
#     def enter(self):
#         a = self.loginLineEdit.text()
#         s = get_without_failing(LoginData, (LoginData.login == a))
#         print(s)
#         if s and s.password == self.passwordLineEdit.text():
#             print('Вход выполнен')
#             self.main_window = MainWindow()
#             self.main_window.show()
#             self.hide()
#
#     def register(self):
#         self.register_window = Register()
#         self.register_window.show()
#
#
# class Register(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('ui/register.ui', self)
#         self.setWindowTitle('Register')
#         self.setWindowIcon(QIcon(ICON))
#         self.registerButton.clicked.connect(self.main)
#         self.loginLineEdit.setPlaceholderText('Please enter login')
#         self.passwordLineEdit.setPlaceholderText('Please enter password')
#         self.passwordLineEdit2.setPlaceholderText('Please enter password again')
#         self.firstNameLineEdit.setPlaceholderText('Please enter first name')
#         self.lastNameLineEdit.setPlaceholderText('Please enter last name')
#
#         self.passwordLineEdit.setEchoMode(QLineEdit.Password)
#         self.passwordLineEdit2.setEchoMode(QLineEdit.Password)
#
#     def check_valid(self, login, pass1, pass2, fname, lname):
#         if not (login and pass1 and pass2 and fname and lname):
#             self.validLabel.setText('Заполните все поля')
#             return False
#         if get_without_failing(LoginData, (LoginData.login == login)):
#             self.validLabel.setText('Такой логин уже используется')
#             return False
#         if pass1 != pass2:
#             self.validLabel.setText('Пароли не совпадают')
#             return False
#         return True
#
#     def main(self):
#         self.validLabel.setText('')
#         login, pass1, pass2 = self.loginLineEdit.text(), self.passwordLineEdit.text(), self.passwordLineEdit2.text()
#         first_name, last_name = self.firstNameLineEdit.text().capitalize(), self.lastNameLineEdit.text().capitalize()
#         if not self.check_valid(login, pass1, pass2, first_name, last_name):
#             return
#         a = self.comboBox.currentText()
#         member = LoginData(login=login, password=pass1)
#         member.save()
#         if a == 'Администратор':
#             member = Doctor(first_name=first_name, last_name=last_name, login=login)
#         else:
#             member = Admin(first_name=first_name, last_name=last_name, login=login)
#         member.save()
#         self.hide()


class Enter(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/enter1.ui', self)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon(ICON))
        self.admin_push_button.clicked.connect(self.set_admin_user)
        self.user_position = POSITIONS[Admin]
        self.get_usernames()

    def set_admin_user(self):
        self.user_position = POSITIONS[Admin]
        self.get_usernames()

    def set_doctor_user(self):
        self.user_position = POSITIONS[Doctor]
        self.get_usernames()

    def get_usernames(self):
        s = get_without_failing(DATABESES_KEYS[self.user_position], (DATABESES_KEYS[self.user_position].id))
        for i in s:
            print(
                f'{i.last_name.capitalize()} {i.first_name[0].upper()}. {i.middle_name[0].upper() if i.middle_name else ""}.')
