from PyQt5 import QtWidgets
from interface import Ui_MainWindow

from myrandom.generators.table.gen import gen as t_gen
from myrandom.generators.algo.gen import gen as a_gen


from PyQt5.QtWidgets import QMessageBox

from myrandom.testing.leonov_method import leonov_check


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
        self.ui.gen_button.clicked.connect(self.gen_seqs)
        self.ui.calc_button.clicked.connect(self.check_seqs)

    def gen_seqs(self) -> None:
        self.__gen_algo(1000)
        self.__gen_tabular(1000)

    def check_seqs(self) -> None:
        try:
            manual_data = self.__get_column(self.ui.manual_table_widget, 0)
        except:
            pass
        algoX_data = self.__get_column(self.ui.algo_table_widget, 0)
        algoXX_data = self.__get_column(self.ui.algo_table_widget, 1)
        algoXXX_data = self.__get_column(self.ui.algo_table_widget, 2)
        tabularX_data = self.__get_column(self.ui.table_table_widget, 0)
        tabularXX_data = self.__get_column(self.ui.table_table_widget, 1)
        tabularXXX_data = self.__get_column(self.ui.table_table_widget, 2)

        try:
            self.ui.manual_k_label.setText(
                "Коэф. случайности K:"+str(leonov_check(manual_data)))
        except:
            pass

        self.ui.algo_k1_label.setText(
            "Коэф. случайности K1:" + str(leonov_check(algoX_data)))
        self.ui.algo_k2_label.setText(
            "Коэф. случайности K2:"+str(leonov_check(algoXX_data)))
        self.ui.algo_k3_label.setText(
            "Коэф. случайности K3:"+str(leonov_check(algoXXX_data)))
        self.ui.table_k1_label.setText(
            "Коэф. случайности K1:"+str(leonov_check(tabularX_data)))
        self.ui.table_k2_label.setText(
            "Коэф. случайности K2:"+str(leonov_check(tabularXX_data)))
        self.ui.table_k3_label.setText(
            "Коэф. случайности K3:"+str(leonov_check(tabularXXX_data)))

    def __get_column(self, t: QtWidgets.QTableWidget, column_i: int) -> list[int]:
        data = []
        for i in range(t.rowCount()):
            data.append(int(t.item(i, column_i).text()))
        print(data)
        return data

    def __gen_tabular(self, size: int) -> None:
        arrayX = t_gen(size, 1)
        arrayXX = t_gen(size, 2)
        arrayXXX = t_gen(size, 3)

        self.ui.table_table_widget.setRowCount(0)

        for i in range(size):
            self.ui.table_table_widget.insertRow(i)
            self.ui.table_table_widget.setItem(
                i, 0, QtWidgets.QTableWidgetItem(str(arrayX[i])))
            self.ui.table_table_widget.setItem(
                i, 1, QtWidgets.QTableWidgetItem(str(arrayXX[i])))
            self.ui.table_table_widget.setItem(
                i, 2, QtWidgets.QTableWidgetItem(str(arrayXXX[i])))

    def __gen_algo(self, size: int) -> None:
        arrayX = a_gen(size, 0, 9)
        arrayXX = a_gen(size, 10, 99)
        arrayXXX = a_gen(size, 100, 999)

        self.ui.algo_table_widget.setRowCount(0)

        for i in range(size):
            self.ui.algo_table_widget.insertRow(i)
            self.ui.algo_table_widget.setItem(
                i, 0, QtWidgets.QTableWidgetItem(str(arrayX[i])))
            self.ui.algo_table_widget.setItem(
                i, 1, QtWidgets.QTableWidgetItem(str(arrayXX[i])))
            self.ui.algo_table_widget.setItem(
                i, 2, QtWidgets.QTableWidgetItem(str(arrayXXX[i])))
