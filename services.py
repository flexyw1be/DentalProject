from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import get_without_failing
from PyQt5.QtWidgets import QApplication
from data.config import *
from error import Error


class Service(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(SERVICE_UI, self)
        self.setWindowTitle('Добавление услуг')
        self.setWindowIcon(QIcon(ICON))
        self.type = 'service'

        self.services_push_button.clicked.connect(self.set_services)
        self.preparations_push_button.clicked.connect(self.set_preparations)

        self.add_push_button.clicked.connect(self.add_service)
        self.set_list_widget()
        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : lightgrey;"
                                                "}")

        self.error_widget = Error('')
        self.error_widget.accept_push_button.clicked.connect(self.ok)

    def set_services(self):
        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : lightgrey;"
                                                "}")
        self.preparations_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : white;"
                                                    "}")
        self.type = 'service'
        self.set_list_widget()

    def set_preparations(self):
        self.services_push_button.setStyleSheet("QPushButton"
                                                "{"
                                                "background-color : white;"
                                                "}")
        self.preparations_push_button.setStyleSheet("QPushButton"
                                                    "{"
                                                    "background-color : lightgrey;"
                                                    "}")
        self.type = 'preparations'
        self.set_list_widget()

    def add_service(self):
        if not self.check_line_edits():
            self.error_widget.label.setText('Проверьте правильность введенных данных')
            self.error_widget.show()
            return
        if self.type == 'service':
            Services.create(article=self.article_line_edit.text(), name=self.name_line_edit.text())
        else:
            Preparations.create(article=self.article_line_edit.text(), name=self.name_line_edit.text())
        Price.create(article=self.article_line_edit.text(), price=self.price_line_edit.text())
        self.set_list_widget()
        self.error_widget.label.setText('Успешно')
        self.error_widget.show()

    def set_list_widget(self):
        self.list_widget.clear()
        if self.type == 'service':
            s = get_without_failing(Services, Services.id)
        else:
            s = get_without_failing(Preparations, Preparations.id)
        if s:
            for i in s:
                self.list_widget.addItem(i.name)

    def check_line_edits(self):
        return len(self.article_line_edit.text()) > 0 and len(self.name_line_edit.text()) > 0 and len(
            self.price_line_edit.text()) > 0

    def ok(self):
        self.error_widget.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ex = Service()
    sys.excepthook = except_hook
    main_ex.show()
    sys.exit(app.exec())
