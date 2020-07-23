import sys
from CalcTPutUI import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from functions import imprime

class CalcTPUT(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnCalcTPut.clicked.connect(self.calc_action)

    def calc_action(self):
        imprime()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calctput = CalcTPUT()
    calctput.show()
    qt.exec_()
