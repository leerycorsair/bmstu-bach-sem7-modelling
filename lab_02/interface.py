# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 503)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(870, 503))
        MainWindow.setMaximumSize(QtCore.QSize(870, 503))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_inmtr = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_inmtr.setFont(font)
        self.label_inmtr.setObjectName("label_inmtr")
        self.verticalLayout.addWidget(self.label_inmtr)
        self.table_inmtr = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_inmtr.sizePolicy().hasHeightForWidth())
        self.table_inmtr.setSizePolicy(sizePolicy)
        self.table_inmtr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_inmtr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_inmtr.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_inmtr.setAlternatingRowColors(True)
        self.table_inmtr.setGridStyle(QtCore.Qt.SolidLine)
        self.table_inmtr.setObjectName("table_inmtr")
        self.table_inmtr.setColumnCount(10)
        self.table_inmtr.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(1, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(2, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(3, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(4, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(5, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(6, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(7, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(8, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_inmtr.setItem(9, 9, item)
        self.table_inmtr.horizontalHeader().setCascadingSectionResizes(False)
        self.table_inmtr.horizontalHeader().setDefaultSectionSize(50)
        self.table_inmtr.horizontalHeader().setSortIndicatorShown(False)
        self.table_inmtr.horizontalHeader().setStretchLastSection(False)
        self.table_inmtr.verticalHeader().setCascadingSectionResizes(False)
        self.table_inmtr.verticalHeader().setDefaultSectionSize(30)
        self.table_inmtr.verticalHeader().setMinimumSectionSize(30)
        self.table_inmtr.verticalHeader().setSortIndicatorShown(False)
        self.table_inmtr.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.table_inmtr)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lb_inmtr_size = QtWidgets.QLabel(self.centralwidget)
        self.lb_inmtr_size.setObjectName("lb_inmtr_size")
        self.horizontalLayout.addWidget(self.lb_inmtr_size)
        self.sb_inmtr_size = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_inmtr_size.sizePolicy().hasHeightForWidth())
        self.sb_inmtr_size.setSizePolicy(sizePolicy)
        self.sb_inmtr_size.setMinimum(1)
        self.sb_inmtr_size.setMaximum(10)
        self.sb_inmtr_size.setObjectName("sb_inmtr_size")
        self.horizontalLayout.addWidget(self.sb_inmtr_size)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.random_inmtr_button = QtWidgets.QPushButton(self.centralwidget)
        self.random_inmtr_button.setObjectName("random_inmtr_button")
        self.verticalLayout.addWidget(self.random_inmtr_button)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_res = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lb_res.setFont(font)
        self.lb_res.setObjectName("lb_res")
        self.verticalLayout_2.addWidget(self.lb_res)
        self.table_resmtr = QtWidgets.QTableWidget(self.centralwidget)
        self.table_resmtr.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_resmtr.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_resmtr.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_resmtr.setObjectName("table_resmtr")
        self.table_resmtr.setColumnCount(2)
        self.table_resmtr.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_resmtr.setHorizontalHeaderItem(1, item)
        self.table_resmtr.horizontalHeader().setDefaultSectionSize(120)
        self.verticalLayout_2.addWidget(self.table_resmtr)
        self.res_button = QtWidgets.QPushButton(self.centralwidget)
        self.res_button.setObjectName("res_button")
        self.verticalLayout_2.addWidget(self.res_button)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.verticalLayout_2.addWidget(self.clear_button)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Марковские цепи"))
        self.label_inmtr.setText(_translate("MainWindow", "Матрица интенсивностей"))
        item = self.table_inmtr.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "S1"))
        item = self.table_inmtr.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "S2"))
        item = self.table_inmtr.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "S3"))
        item = self.table_inmtr.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "S4"))
        item = self.table_inmtr.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "S5"))
        item = self.table_inmtr.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "S6"))
        item = self.table_inmtr.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "S7"))
        item = self.table_inmtr.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "S8"))
        item = self.table_inmtr.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "S9"))
        item = self.table_inmtr.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "S10"))
        item = self.table_inmtr.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "S1"))
        item = self.table_inmtr.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "S2"))
        item = self.table_inmtr.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "S3"))
        item = self.table_inmtr.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "S4"))
        item = self.table_inmtr.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "S5"))
        item = self.table_inmtr.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "S6"))
        item = self.table_inmtr.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "S7"))
        item = self.table_inmtr.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "S8"))
        item = self.table_inmtr.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "S9"))
        item = self.table_inmtr.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S10"))
        __sortingEnabled = self.table_inmtr.isSortingEnabled()
        self.table_inmtr.setSortingEnabled(False)
        item = self.table_inmtr.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(0, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(1, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(2, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(3, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(4, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(5, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(6, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(7, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(8, 9)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 0)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 1)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 2)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 3)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 5)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 6)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 7)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 8)
        item.setText(_translate("MainWindow", "0"))
        item = self.table_inmtr.item(9, 9)
        item.setText(_translate("MainWindow", "0"))
        self.table_inmtr.setSortingEnabled(__sortingEnabled)
        self.lb_inmtr_size.setText(_translate("MainWindow", "Количество состояний"))
        self.random_inmtr_button.setText(_translate("MainWindow", "Случайное заполнение"))
        self.lb_res.setText(_translate("MainWindow", "Ответ"))
        item = self.table_resmtr.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "S1"))
        item = self.table_resmtr.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "S2"))
        item = self.table_resmtr.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "S3"))
        item = self.table_resmtr.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "S4"))
        item = self.table_resmtr.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "S5"))
        item = self.table_resmtr.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "S6"))
        item = self.table_resmtr.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "S7"))
        item = self.table_resmtr.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "S8"))
        item = self.table_resmtr.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "S9"))
        item = self.table_resmtr.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "S10"))
        item = self.table_resmtr.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Вероятность P"))
        item = self.table_resmtr.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Время t"))
        self.res_button.setText(_translate("MainWindow", "Вычислить"))
        self.clear_button.setText(_translate("MainWindow", "Очистить все"))
