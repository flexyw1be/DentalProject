import sys

from PyQt5.QtWidgets import QApplication
from main import Enter


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_ex = Enter()
    sys.excepthook = except_hook
    main_ex.show()
    sys.exit(app.exec())
