from PyQt5 import QtWidgets, QtCore
from interface import Ui_MainWindow
from PyQt5.QtGui import QResizeEvent
import pyqtgraph as pg

from mathematics import calc_ud_cdf,  calc_ud_pdf, calc_erlang_pdf, calc_erlang_cdf


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
        self.ui.ud_button.clicked.connect(self.ud_draw)
        self.ui.erlang_button.clicked.connect(self.erlang_draw)

        self.ui.author_button.clicked.connect(self.info_creator)
        self.ui.prog_button.clicked.connect(self.info_program)

    def ud_draw(self) -> None:
        try:
            left, right = (float(self.ui.entry_left.text()),
                           float(self.ui.entry_right.text()))
            a, b = (float(self.ui.entry_a.text()),
                    float(self.ui.entry_b.text()))
            if left >= right or a >= b:
                QMessageBox.warning(
                    self, "Ошибка", "Некорректные границы или параметры")
                raise
            pen = pg.mkPen(color=(255, 0, 0), width=3)
            self.ui.cdf.clear()
            self.ui.cdf.addLegend()
            self.ui.cdf.plot(*calc_ud_cdf(left, right, a, b),
                             pen=pen, name=f'(a = {a}, b = {b})')
            self.ui.pdf.clear()
            self.ui.pdf.addLegend()
            self.ui.pdf.plot(*calc_ud_pdf(left, right, a, b),
                             pen=pen, name=f'(a = {a}, b = {b})')
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Некорректный ввод")
        except:
            QMessageBox.warning(self, "Ошибка", "Неизвестная ошибка")

    def erlang_draw(self) -> None:
        try:
            max = float(self.ui.entry_max.text())
            k, theta = (int(self.ui.entry_k.text()),
                        float(self.ui.entry_theta.text()))
            if max <= 0 or k <= 0 or theta < 0:
                QMessageBox.warning(
                    self, "Ошибка", "Некорректные границы или параметры")
                raise
            pen = pg.mkPen(color=(255, 0, 0), width=3)
            self.ui.cdf.clear()
            self.ui.cdf.addLegend()
            self.ui.cdf.plot(*calc_erlang_cdf(max, k, theta),
                             pen=pen, name=f'(k = {k},  θ = {theta})')
            self.ui.pdf.clear()
            self.ui.pdf.addLegend()
            self.ui.pdf.plot(*calc_erlang_pdf(max, k, theta),
                             pen=pen, name=f'(k = {k},  θ = {theta})')
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Некорректный ввод")
        except:
            QMessageBox.warning(self, "Ошибка", "Неизвестная ошибка")

    def info_creator(self) -> None:
        title = "Об авторе"
        msg = '''Программа создана Леоновым Владиславом

vk.com/leerycorsair
t.me/leerycorsair
        '''
        QMessageBox.about(self, title, msg)

    def info_program(self) -> None:
        title = "О программе"
        msg = '''Версия:1.0.0
PyQt:5.15.7
NumPy:1.22.3

Программа создана в рамках учебного курса по моделированию

(c) Лицензия МГТУ v1.1
        '''
        QMessageBox.about(self, title, msg)

    def resizeEvent(self, event: QResizeEvent) -> None:
        return super().resizeEvent(event)
