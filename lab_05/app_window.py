from PyQt5 import QtWidgets
from interface import Ui_MainWindow

from model.base_generator import BaseGenerator
from model.request import RequestGenerator, RequestProcessor
from model.model import Model


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
        self.ui.calc_button.clicked.connect(self.calc)

    def calc(self) -> None:
        try:
            generator = RequestGenerator(
                BaseGenerator(
                    float(self.ui.clients_time_entry.text()),
                    float(self.ui.clients_delta_entry.text())),
                int(self.ui.clients_amount_entry.text()))

            operators = [
                RequestProcessor(
                    BaseGenerator(
                        float(self.ui.op1_time_entry.text()),
                        float(self.ui.op1_delta_entry.text())),
                    max_queue_size=1),
                RequestProcessor(
                    BaseGenerator(
                        float(self.ui.op2_time_entry.text()),
                        float(self.ui.op2_delta_entry.text())),
                    max_queue_size=1),
                RequestProcessor(
                    BaseGenerator(
                        float(self.ui.op3_time_entry.text()),
                        float(self.ui.op3_delta_entry.text())),
                    max_queue_size=1)]

            computers = [
                RequestProcessor(
                    BaseGenerator(
                        float(self.ui.comp1_entry.text()))),
                RequestProcessor(
                    BaseGenerator(
                        float(self.ui.comp2_entry.text())))]

            model = Model(generator, operators, computers)
            result = model.event_mode()

            msg = QMessageBox()
            msg.setWindowTitle("Ответ")
            msg.setText("Потеряно заявок:{:<5.2g}\nПроцент потерь:{:<5.2g}".format(
                result["lost"], result["lost_percentage"]))
            msg.exec()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Некорретный ввод!")
            msg.exec()
