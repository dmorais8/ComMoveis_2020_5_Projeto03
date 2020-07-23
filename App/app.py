import sys
from CalcTPutUI import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from functions import calc_troughtput_from_table


class CalcTPUT(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)

        self.btnCalcTPut.clicked.connect(self.calc_troughput)

    def calc_troughput(self):

        bandwidth = self.comboBanda.currentText()
        mcs = self.comboMCS.currentText()
        mimo = self.ComboMimo.currentText()
        cp = self.comboPrefixCycle.currentText()
        ca = self.comboCarrierAgg.currentText()

        print(f'BANDA: {bandwidth}')
        print(f'MCS: {mcs}')
        print(f'MIMO: {mimo}')
        print(f'CP: {cp}')
        print(f'CA: {ca}')

        troughput = calc_troughtput_from_table(bandwidth, mcs, mimo, cp, ca)
        print(f'{troughput} Mbps')
        self.outputTabela.setText(f'{troughput} Mbps')


if __name__ == '__main__':

    qt = QApplication(sys.argv)
    calctput = CalcTPUT()
    calctput.show()
    qt.exec_()
