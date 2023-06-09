# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1139, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.cdf = pg.PlotWidget(self.centralwidget)
        self.cdf.setTitle("Фукнция распределения F(x)")
        self.cdf.setBackground('w')
        self.pdf = pg.PlotWidget(self.centralwidget)
        self.pdf.setTitle("Фукнция плотности f(x)")
        self.pdf.setBackground('w')

        # self.cdf = QtWidgets.QGraphicsView(self.centralwidget)
        self.cdf.setObjectName("cdf")
        self.horizontalLayout.addWidget(self.cdf)
        # self.pdf = QtWidgets.QGraphicsView(self.centralwidget)
        self.pdf.setObjectName("pdf")
        self.horizontalLayout.addWidget(self.pdf)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.entry_left = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_left.setWhatsThis("")
        self.entry_left.setText("")
        self.entry_left.setPlaceholderText("")
        self.entry_left.setObjectName("entry_left")
        self.verticalLayout_6.addWidget(self.entry_left)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.entry_right = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_right.setObjectName("entry_right")
        self.verticalLayout_6.addWidget(self.entry_right)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.entry_a = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_a.setObjectName("entry_a")
        self.verticalLayout_5.addWidget(self.entry_a)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.entry_b = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_b.setObjectName("entry_b")
        self.verticalLayout_5.addWidget(self.entry_b)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.ud_button = QtWidgets.QPushButton(self.centralwidget)
        self.ud_button.setObjectName("ud_button")
        self.verticalLayout_7.addWidget(self.ud_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 2, 2)
        self.entry_max = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_max.setObjectName("entry_max")
        self.gridLayout.addWidget(self.entry_max, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.entry_k = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_k.setObjectName("entry_k")
        self.gridLayout.addWidget(self.entry_k, 2, 0, 1, 1)
        self.entry_theta = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_theta.setObjectName("entry_theta")
        self.gridLayout.addWidget(self.entry_theta, 4, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.erlang_button = QtWidgets.QPushButton(self.centralwidget)
        self.erlang_button.setObjectName("erlang_button")
        self.verticalLayout_3.addWidget(self.erlang_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.prog_button = QtWidgets.QPushButton(self.centralwidget)
        self.prog_button.setObjectName("prog_button")
        self.verticalLayout_4.addWidget(self.prog_button)
        self.author_button = QtWidgets.QPushButton(self.centralwidget)
        self.author_button.setObjectName("author_button")
        self.verticalLayout_4.addWidget(self.author_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Равномерное распределение"))
        self.label.setText(_translate("MainWindow", "Левая граница"))
        self.label_2.setText(_translate("MainWindow", "Правая граница"))
        self.label_4.setText(_translate("MainWindow", "Параметр 𝘢"))
        self.label_5.setText(_translate("MainWindow", "Параметр 𝘣"))
        self.ud_button.setText(_translate("MainWindow", "Построить"))
        self.label_6.setText(_translate("MainWindow", "Распредление Эрланга"))
        self.label_9.setText(_translate("MainWindow", "Максимальное значение"))
        self.label_7.setText(_translate("MainWindow", "Параметр 𝘬"))
        self.label_8.setText(_translate("MainWindow", "Параметр θ"))
        self.erlang_button.setText(_translate("MainWindow", "Построить"))
        self.prog_button.setText(_translate("MainWindow", "О программе"))
        self.author_button.setText(_translate("MainWindow", "Об авторе"))
