from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
from data.all_models import *
from MainWindow import *



def get_without_failing(Model, query):
    results = Model.select().where(query).limit(1)
    return results[0] if len(results) > 0 else None


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/start.ui', self)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon('data/deltadent1.png'))
        self.loginButton.setEnabled(False)
        self.loginLineEdit.setPlaceholderText('Please enter your login')
        self.passwordLineEdit.setPlaceholderText('Please enter your password')
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.loginLineEdit.textChanged.connect(self.check_input)
        self.passwordLineEdit.textChanged.connect(self.check_input)

        self.loginButton.clicked.connect(self.enter)
        self.registerButton.clicked.connect(self.register)

    def check_input(self):
        if self.loginLineEdit.text() and self.passwordLineEdit.text():
            self.loginButton.setEnabled(True)
        else:
            self.loginButton.setEnabled(False)

    def enter(self):
        a = self.loginLineEdit.text()
        s = get_without_failing(LoginData, (LoginData.login == a))
        print(s)
        if s and s.password == self.passwordLineEdit.text():
            print('Вход выполнен')
            self.main_window = MainWindow()
            self.main_window.show()
            self.hide()


    def register(self):
        self.register_window = Register()
        self.register_window.show()




class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/register.ui', self)
        self.setWindowTitle('Register')
        self.setWindowIcon(QIcon('data/deltadent1.png'))

        self.loginLineEdit.setPlaceholderText('Please enter login')
        self.passwordLineEdit.setPlaceholderText('Please enter password')
        self.passwordLineEdit_2.setPlaceholderText('Please enter password again')






