from PyQt5 import QtWidgets
from interface import Ui_MainWindow

from distr.erlang import ErlangDistribution
from distr.uniform import UniformDistribution

from models.time_model import TimeModel
from models.event_model import EventModel


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
            generator = UniformDistribution(
                float(self.ui.gen_left_entry.text()),
                float(self.ui.gen_right_entry.text())
            )

            processor = ErlangDistribution(
                float(self.ui.proc_alpha_entry.text()),
                float(self.ui.proc_beta_entry.text()),
                0
            )

            step = float(self.ui.step_entry.text())
            total_req = float(self.ui.req_entry.text())
            rate = int(self.ui.rate_entry.text())

            tm = TimeModel(generator, processor, step)
            em = EventModel(generator, processor)

            self.ui.min_time_entry.setText(str(tm.start(total_req, rate)))
            self.ui.min_event_entry.setText(str(em.start(total_req, rate)))
        except:
            pass

       