# demoform.ui : 화면구성, demoform.py : 로직단

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

form_class = uic.loadUiType("demoForm.ui")[0]

class Demoform(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoform = Demoform()
    demoform.show()
    app.exec_()


