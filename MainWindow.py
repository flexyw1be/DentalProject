from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from config import *
from medicalCard import MedicalCard
from schedule import Schedule


class MainWindow(QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.setWindowIcon(QIcon(ICON))
        self.user_name = name
        print(self.user_name)
        self.setWindowTitle('DentalProject')
        self.firstTimeComboBox.addItems([f'{x}:00' for x in range(START_TIME, FINISH_TIME)])
        self.firstTimeComboBox.activated[str].connect(self.onActivated)

        self.card_push_button.setStyleSheet("QPushButton"
                                            "{"
                                            "qproperty-icon: url(data/123.jfif);"

                                            "}")
        self.card_push_button.setIconSize(QSize(65, 65))
        self.card_push_button.clicked.connect(self.show_card)
        self.shedule_push_button.clicked.connect(self.show_schedule)

    def exit(self):
        pass

    def settings(self):
        pass

    def onActivated(self):
        n = int(self.firstTimeComboBox.currentText().split(':')[0])
        self.lastTimeComboBox.clear()
        self.lastTimeComboBox.addItems([f'{x}:00' for x in range(n, FINISH_TIME + 1)])

    def show_card(self):
        self.card = MedicalCard()
        self.card.show()

    def show_schedule(self):
        self.schedule = Schedule()
        self.schedule.show()
