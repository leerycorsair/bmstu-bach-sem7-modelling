from PyQt5 import QtWidgets
from interface import Ui_MainWindow

from model.base_generator import BaseGenerator
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
            generator = BaseGenerator(float(self.ui.req_time_entry.text()),
                                      float(self.ui.req_delta_entry.text()))

            operators = {"Default": BaseGenerator(float(self.ui.d_design_time_entry.text()),
                                                  float(self.ui.d_design_delta_entry.text())),
                         "Government": BaseGenerator(float(self.ui.g_design_time_entry.text()),
                                                     float(self.ui.g_design_delta_entry.text()))}
            builders = {"Default": BaseGenerator(float(self.ui.d_built_time_entry.text()),
                                                 float(self.ui.d_built_delta_entry.text())),
                        "Government": BaseGenerator(float(self.ui.g_built_time_entry.text()),
                                                    float(self.ui.g_built_delta_entry.text()))}
            certifiers = {"Default": BaseGenerator(float(self.ui.d_certify_time_entry.text()),
                                                   float(self.ui.d_certify_delta_entry.text())),
                          "Government": BaseGenerator(float(self.ui.g_certify_time_entry.text()),
                                                      float(self.ui.g_certify_delta_entry.text()))}

            model = Model(generator, operators, builders, certifiers)
            processed_tasks, lost_tasks = model.start(int(self.ui.req_quan_entry.text()),
                                                      int(self.ui.g_rate_entry.text()),
                                                      int(self.ui.g_rrate_entry.text()),
                                                      int(self.ui.d_rrate_entry.text()))

            msg = QMessageBox()
            msg.setWindowTitle("Ответ")
            text = "Выполнено гражданских заявок:{}\n".format(
                processed_tasks["Default"]) + "Выполнено ведоственных заявок:{}\n".format(
                processed_tasks["Government"]) + "Упущено гражданских заявок:{}\n".format(
                lost_tasks["Default"]) + "Упущено ведомственных заявок:{}\n".format(
                lost_tasks["Government"])
            msg.setText(text)
            msg.exec()

        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Некорретный ввод!")
            msg.exec()
