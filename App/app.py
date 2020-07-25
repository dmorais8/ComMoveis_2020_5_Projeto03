import sys
from pathlib import Path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from Interface.CalcTPutUI import *
from functions import calc_lte_troughtput

data_folder = Path("assets/")
icon = data_folder / "lte-icon.png"


class CalcTPUT(QMainWindow, Ui_MainWindow):

    """
        Classe que instacia e faz utilizacao dos componentes da interface
    """

    def __init__(self, parent=None):

        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Calculadora LTE-Advanced')
        self.setWindowIcon(QIcon("lte-icon.png"))

        # Pega o acionamento do bota Calcular da inteface e chama metodo calc_button_action()
        self.btnCalcTPut.clicked.connect(self.calc_button_action)

    def calc_button_action(self):

        """
        Metodo que colhe os valores dos campos na interface, chama a funcao de calculo do throughtput e retorna o valor
        na interface.
        :return:
        """

        bandwidth = self.comboBanda.currentText()
        mcs = self.comboMCS.currentText()
        mimo = self.ComboMimo.currentText()
        cp = self.comboPrefixCycle.currentText()
        ca = self.comboCarrierAgg.currentText()

        # Executa o calculo do throughput por meio da funcao calc_lte_troughtput
        calc_data = calc_lte_troughtput(bandwidth, mcs, mimo, cp, ca)

        try:

            self.outputPRB.setAlignment(QtCore.Qt.AlignCenter)
            self.outputPRB.setText(str(calc_data['PRBS']))

            self.outputTbsIndex.setAlignment(QtCore.Qt.AlignCenter)
            self.outputTbsIndex.setText(str(calc_data['TBSINDEX']))

            self.ouputTbsValue.setAlignment(QtCore.Qt.AlignCenter)
            self.ouputTbsValue.setText(str(calc_data['TBSVALUE']))

            self.outputModulacao.setAlignment(QtCore.Qt.AlignCenter)
            self.outputModulacao.setText(str(calc_data['MODULATION']) + 'QAM' if calc_data['MODULATION'] >= 16 else 'QPSK')

            self.outputNumRE.setAlignment(QtCore.Qt.AlignCenter)
            self.outputNumRE.setText(str(calc_data['NRE']))

            self.outputQtdSimbolos.setAlignment(QtCore.Qt.AlignCenter)
            self.outputQtdSimbolos.setText(str(calc_data['SYMBOLSQTD']))

            self.outputTabela.setText(f'{calc_data["TROUGHPUT_TABLE"]} Mbps')
            self.outputEquacao.setText(f'{calc_data["TROUGHPUT_EQUATION"]} Mbps')

        except TypeError as e:
            sys.exit(1)


if __name__ == '__main__':

    qt = QApplication(sys.argv)
    calctput = CalcTPUT()
    calctput.show()
    qt.exec_()
