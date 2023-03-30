from PyQt5 import QtWidgets, QtCore
from interface import Ui_MainWindow

from mathematics import calc_res, random_mtr


from PyQt5.QtWidgets import QMessageBox


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(AppWindow, self).__init__()
        self.ui_setup()

    def ui_setup(self) -> None:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.bind_buttons()
        self.show()

    def bind_buttons(self) -> None:
        self.ui.clear_button.clicked.connect(self.clear_all)
        self.ui.res_button.clicked.connect(self.res_calc)
        self.ui.random_inmtr_button.clicked.connect(self.random_inmtr)

    def clear_all(self) -> None:
        self.ui.table_inmtr.clearContents()
        self.ui.table_resmtr.clearContents()

    def res_calc(self) -> None:
        try:
            size = self.ui.sb_inmtr_size.value()
            inmtr = [[float(self.ui.table_inmtr.item(i, j).text())
                      for j in range(size)] for i in range(size)]

            res = calc_res(inmtr)
            for i in range(size):
                prob_cell = QtWidgets.QTableWidgetItem(
                    str(round(res[0][i], 5)))
                time_cell = QtWidgets.QTableWidgetItem(
                    str(round(res[1][i], 5)))

                self.ui.table_resmtr.setItem(i, 0, prob_cell)
                self.ui.table_resmtr.setItem(i, 1, time_cell)

        except:
            QMessageBox.warning(self, "Предупреждение", "Некорректный ввод")

    def random_inmtr(self) -> None:
        try:
            size = self.ui.sb_inmtr_size.value()
            inmtr = random_mtr(size)
            self.ui.table_inmtr.clearContents()
            for i in range(size):
                for j in range(size):
                    current_cell = QtWidgets.QTableWidgetItem(str(inmtr[i][j]))
                    self.ui.table_inmtr.setItem(i, j, current_cell)
        except:
            QMessageBox.warning(self, "Предупреждение", "Некорректный ввод")
