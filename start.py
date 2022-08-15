import sys

from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from main import Login


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ex = Login()
    sys.excepthook = except_hook
    main_ex.show()
    # main_ex.app()
    sys.exit(app.exec())


