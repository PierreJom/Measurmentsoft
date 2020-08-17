# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fenetre.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox
from decimal import *
import threading
import Automate
import Mesure
import Parcourir
import time

axis1 = ''
axis2 = ''
step = 0
Pmin1 = 0
Pmax1 = 0
Pmin2 = 0
Pmax2 = 0
PasF = 0
Pas1 = 0
Pas2 = 1
Fnb = Mesure.NBsweepPoint_Req()
Nb1 = 0
Nb2 = 0
Form1 = 0
Form2 = 0
S11 = 0
S22 = 0
S12 = 0
S21 = 0
FreqD = 0
FreqF = 0
prog = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)

        self.line.setGeometry(QtCore.QRect(-20, 300, 1031, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 190, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 190, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 190, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 190, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 190, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 190, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(380, 220, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(370, 30, 101, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(184, 150, 81, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(380, 250, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(370, 150, 81, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(580, 150, 81, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(110, 580, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(110, 780, 75, 23))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(840, 810, 150, 23))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(900, 740, 75, 23))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(840, 780, 150, 23))
        self.pushButton_19.setObjectName("pushButton_19")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(280, 360, 421, 211))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(280, 630, 421, 211))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(10, 860, 981, 91))
        self.listView_3.setObjectName("listView_3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(200, 80, 471, 21))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 340, 161, 21))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 450, 171, 21))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(780, 380, 101, 51))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")

        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 0, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(390, 0, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 0, 31, 21))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 0, 31, 21))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.radioButton_6.setGeometry(QtCore.QRect(100, 0, 31, 21))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.radioButton_7.setGeometry(QtCore.QRect(0, 0, 31, 21))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.radioButton_8.setGeometry(QtCore.QRect(60, 0, 31, 21))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.radioButton_9.setGeometry(QtCore.QRect(110, 0, 31, 21))
        self.radioButton_9.setObjectName("radioButton_9")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 370, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 400, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 430, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 670, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 700, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 730, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 110, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 110, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(560, 110, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(370, 191, 101, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(100, 480, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(100, 510, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(100, 540, 111, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(712, 740, 181, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setGeometry(QtCore.QRect(930, 460, 41, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(782, 780, 51, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 370, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 400, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 540, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 630, 120, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(780, 360, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 670, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 700, 21, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(5, 730, 100, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 480, 41, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 510, 21, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(720, 460, 211, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(70, 430, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(300, 585, 100, 23))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(500, 585, 300, 23))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(750, 480, 300, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(280, 110, 47, 13))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(470, 110, 47, 13))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(680, 110, 47, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(220, 370, 47, 13))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(220, 400, 47, 13))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(220, 430, 47, 13))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(220, 480, 47, 13))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(220, 510, 47, 13))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(220, 540, 47, 13))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(220, 670, 47, 13))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(220, 700, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(710, 780, 71, 16))
        self.label_28.setObjectName("label_28")

        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(0, 0, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 30, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 0, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(50, 30, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(750, 500, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(830, 500, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.T1)
        self.pushButton_2.clicked.connect(self.T2)
        self.pushButton_3.clicked.connect(self.T3)
        self.pushButton_4.clicked.connect(self.T4)
        self.pushButton_5.clicked.connect(self.T5)
        self.pushButton_6.clicked.connect(self.T6)
        self.pushButton_7.clicked.connect(self.T7)
        self.pushButton_8.clicked.connect(self.T8)
        self.pushButton_9.clicked.connect(self.T9)
        self.pushButton_10.clicked.connect(self.T10)
        self.pushButton_11.clicked.connect(self.T11)
        self.pushButton_12.clicked.connect(self.B12)
        self.pushButton_13.clicked.connect(self.T13)
        self.pushButton_14.clicked.connect(self.T14)
        self.pushButton_15.clicked.connect(self.T15)
        self.pushButton_16.clicked.connect(self.T16)
        self.pushButton_17.clicked.connect(self.T17)
        self.pushButton_18.clicked.connect(self.Parcourir)
        self.pushButton_19.clicked.connect(self.T19)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_5.setText(_translate("MainWindow", "Excel"))
        self.checkBox_6.setText(_translate("MainWindow", "Marker"))
        self.label_16.setText(_translate("MainWindow", "Format exportation :"))
        self.label_12.setText(_translate("MainWindow", "Temps entre chaque mesure (sec):"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "10"))
        self.pushButton_4.setText(_translate("MainWindow", "50"))
        self.pushButton_5.setText(_translate("MainWindow", "-50"))
        self.pushButton_6.setText(_translate("MainWindow", "-10"))
        self.pushButton_7.setText(_translate("MainWindow", "-5"))
        self.pushButton_8.setText(_translate("MainWindow", "-1"))
        self.pushButton_9.setText(_translate("MainWindow", "set"))
        self.radioButton_3.setText(_translate("MainWindow", "z"))
        self.radioButton.setText(_translate("MainWindow", "x"))
        self.radioButton_2.setText(_translate("MainWindow", "y"))
        self.pushButton_10.setText(_translate("MainWindow", "Mise a l\'origine"))
        self.pushButton_11.setText(_translate("MainWindow", "Set as 0"))
        self.pushButton_13.setText(_translate("MainWindow", "Set as 0"))
        self.pushButton_14.setText(_translate("MainWindow", "Set as 0"))
        self.label.setText(_translate("MainWindow", "Début :"))
        self.label_2.setText(_translate("MainWindow", "Fin :"))
        self.label_3.setText(_translate("MainWindow", "Pas :"))
        self.label_7.setText(_translate("MainWindow", "Début :"))
        self.label_8.setText(_translate("MainWindow", "Fin :"))
        self.label_9.setText(_translate("MainWindow", "Nombre de points :"))
        self.pushButton_12.setText(_translate("MainWindow", "STOP"))
        self.label_4.setText(_translate("MainWindow", "Position :"))
        self.label_5.setText(_translate("MainWindow", "Fréquence (sweep) :"))
        self.pushButton_15.setText(_translate("MainWindow", "ok"))
        self.pushButton_16.setText(_translate("MainWindow", "ok"))
        self.pushButton_17.setText(_translate("MainWindow", "Lancement de la séquence"))
        self.pushButton_19.setText(_translate("MainWindow", "Prise de mesure unique"))
        self.checkBox.setText(_translate("MainWindow", "S11"))
        self.checkBox_2.setText(_translate("MainWindow", "S12"))
        self.checkBox_3.setText(_translate("MainWindow", "S21"))
        self.checkBox_4.setText(_translate("MainWindow", "S22"))
        self.label_6.setText(_translate("MainWindow", "Mesure souhaité"))
        self.label_10.setText(_translate("MainWindow", "Début :"))
        self.label_11.setText(_translate("MainWindow", "Fin :"))
        self.label_13.setText(_translate("MainWindow", "Pas :"))
        self.radioButton_4.setText(_translate("MainWindow", "x"))
        self.radioButton_6.setText(_translate("MainWindow", "z"))
        self.radioButton_5.setText(_translate("MainWindow", "y"))
        self.radioButton_9.setText(_translate("MainWindow", "z"))
        self.radioButton_8.setText(_translate("MainWindow", "y"))
        self.radioButton_7.setText(_translate("MainWindow", "x"))
        self.pushButton_18.setText(_translate("MainWindow", "Parcourir"))
        self.label_14.setText(_translate("MainWindow", "Etapes"))
        self.label_15.setText(_translate("MainWindow", "Temps"))
        self.label_17.setText(_translate("MainWindow", "mm"))
        self.label_18.setText(_translate("MainWindow", "mm"))
        self.label_19.setText(_translate("MainWindow", "mm"))
        self.label_20.setText(_translate("MainWindow", "mm"))
        self.label_21.setText(_translate("MainWindow", "mm"))
        self.label_22.setText(_translate("MainWindow", "mm"))
        self.label_23.setText(_translate("MainWindow", "mm"))
        self.label_24.setText(_translate("MainWindow", "mm"))
        self.label_25.setText(_translate("MainWindow", "mm"))
        self.label_26.setText(_translate("MainWindow", "GHz"))
        self.label_27.setText(_translate("MainWindow", "GHz"))
        self.label_28.setText(_translate("MainWindow", "Nb de mesure:"))

        self.model1 = QStandardItemModel(self.listView)
        self.model2 = QStandardItemModel(self.listView_2)
        self.model3 = QStandardItemModel(self.listView_3)

    def Format(self):
        global Form1, Form2
        Form1 = 0  # csv
        Form2 = 0  # marker
        if self.checkBox_5.isChecked() and not self.checkBox_6.isChecked():
            Form1 = 1
            self.Check()
            # csv
        if self.checkBox_6.isChecked() and not self.checkBox_5.isChecked():
            Form2 = 1
            Mesure.Marker()
            # marker
        if self.checkBox_5.isChecked() and self.checkBox_6.isChecked():
            Form1 = 1
            Form2 = 1
            self.Check()
            Mesure.Marker()
            # csv + marker

    def Check(self):
        if self.checkBox.isChecked():
            Mesure.S11()
        if self.checkBox_2.isChecked():
            Mesure.S12()
        if self.checkBox_3.isChecked():
            Mesure.S21()
        if self.checkBox_4.isChecked():
            Mesure.S22()

    def Text_AFF1(self, Text):
        item = QStandardItem(Text)
        self.model1.appendRow(item)
        self.listView.setModel(self.model1)
        self.listView.show()

    def Text_AFF2(self, Text):
        item = QStandardItem(Text)
        self.model2.appendRow(item)
        self.listView_2.setModel(self.model2)
        self.listView_2.show()

    def Text_Aff3(self, Text):
        item = QStandardItem(Text)
        self.model3.appendRow(item)
        self.listView_3.setModel(self.model3)
        self.listView_3.show()

    def Text_Aff_Clear(self):
        self.model1.clear()
        self.listView.setModel(self.model1)
        self.listView.show()
        self.model2.clear()
        self.listView_2.setModel(self.model2)
        self.listView_2.show()

        ############################Function PushButton##################################

    def B1(self):
        try:
            self.Selec()
            Automate.Increment_pos(1)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B2(self):
        try:
            self.Selec()
            Automate.Increment_pos(5)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B3(self):
        try:
            self.Selec()
            Automate.Increment_pos(10)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B4(self):
        try:
            self.Selec()
            Automate.Increment_pos(50)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B5(self):
        try:
            self.Selec()
            Automate.Increment_pos(-50)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B6(self):
        try:
            self.Selec()
            Automate.Increment_pos(-10)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B7(self):
        try:
            self.Selec()
            Automate.Increment_pos(-5)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B8(self):
        try:
            self.Selec()
            Automate.Increment_pos(-1)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B9(self):
        try:
            self.Selec()
            iVal = self.lineEdit_10.text()
            Automate.Choix_position(iVal)
            Automate.Reception()
            self.Actu()
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Déplacement impossible")

    def B10(self):
        try:
            Automate.SO()
            self.Text_Aff3("Les axes sont à l'origine")
            Automate.Reception()
            self.Actu()
        except:
            self.Text_Aff3("Déplacement impossible")

    def B11(self):
        try:
            Automate.Choix_Axe(3)
            Automate.Set_origine()
            self.Actu()
            self.Text_Aff3("Cette position sera le 0 de l'axe {}".format(axis))
        except:
            self.Text_Aff3("Erreur mise a 0")

    def B13(self):
        try:
            Automate.Choix_Axe(2)
            Automate.Set_origine()
            self.Actu()
            self.Text_Aff3("Cette position sera le 0 de l'axe {}".format(axis))
        except:
            self.Text_Aff3("Erreur mise a 0")

    def B14(self):
        try:
            Automate.Choix_Axe(1)
            Automate.Set_origine()
            self.Actu()
            self.Text_Aff3("Cette position sera le 0 de l'axe {}".format(axis))
        except:
            self.Text_Aff3("Erreur mise a 0")

    def B12(self):
        global step
        try:
            Automate.STOP()
            if step != 3:
                step = 3
            self.Text_Aff3("Arret du mouvement")
            self.Actu()
            self.Actu()
        except:
            self.Text_Aff3("Déplacement impossible")

    def B15(self):
        try:
            self.Selec1()
            self.Affich1()
            if self.radioButton_7.isChecked() or self.radioButton_8.isChecked() or self.radioButton_9.isChecked():
                self.Selec2()
                self.Affich2()
        except:
            self.Text_Aff3("Déplacement impossible")

    def B19(self):
        try:
            NBM = self.lineEdit_16.text()
            if not NBM:
                NBM = 1
            else:
                NBM = int(NBM)
            Sec = self.lineEdit_15.text()
            if not Sec:
                Sec = 0
            else:
                Sec = int(Sec)
            for x in range(NBM):
                Mesure.HoldToggle()
                self.Format()
                Mesure.STATUS()
                if Mesure.STATUS() is True:
                    Mesure.HoldToggle()
                    time.sleep(Sec)
            self.Actu()
            Automate.Choix_Axe(0)
            self.Text_Aff3("Mesure fini")
        except:
            self.Text_Aff3("Erreur Mesure")

    def B17(self):
        ##########################Fonction Sequence#######################################
        try:
            global flag, step, Val2, Nb2, Nb1, Sec, td, NbT,Pmax2
            Mesure.Holdinit()
            step = 0
            Sec = self.lineEdit_15.text()
            if not Sec:
                Sec = 0
            else:
                Sec = int(Sec)
            self.Selec1()
            self.Affich1()
            Automate.Choix_position(Pmin1)
            Automate.Reception()
            if self.radioButton_7.isChecked() or self.radioButton_8.isChecked() or self.radioButton_9.isChecked():
                time.sleep(.1)
                self.Selec2()
                self.Affich2()
                Automate.Choix_position(Pmin2)
                Automate.Reception()
                time.sleep(Sec)
            else:
                time.sleep(Sec)
                Pmax2 = 0
                Val2 = 0
                Nb2 = 1
            NbT = Nb1 * Nb2
            while step != 3:
                self.label_14.setText(str(NbT) + " points restant")
                self.Selec()
                self.Selec1()
                if self.radioButton_7.isChecked() or self.radioButton_8.isChecked() or self.radioButton_9.isChecked():
                    self.Selec2()
                if float(Val2) >= Pmax2 and NbT is 1:
                    if Val1 >= Pmax1 or Val1 >= -Pmax1:
                        NbT = NbT - 1
                        Mesure.HoldToggle()
                        self.Format()
                        Mesure.STATUS()
                        if Mesure.STATUS() is True:
                            Mesure.HoldToggle()
                            step = 3
                            self.Actu()
                            self.label_14.setText(str(NbT) + " points restant")
                            self.label_15.setText("Temps restant 0 : 0 : 0")
                            Automate.Choix_Axe(0)
                            Mesure.Enregistrer_log()
                            self.Text_Aff3("Séquence finie")
                            self.Text_Aff_Clear()
                if step is 0:
                    self.Selec1()
                    for x in range(int(Pmin1 * 100), int(Pmax1 * 100), int(Pas1 * 100)):
                        NbT = NbT - 1
                        self.label_14.setText(str(NbT) + " points restant")
                        t0 = time.clock()
                        Mesure.HoldToggle()
                        self.Format()
                        Mesure.STATUS()
                        if Mesure.STATUS() is True:
                            Mesure.HoldToggle()
                            self.Selec1()
                            Automate.Increment_pos(Pas1)
                            Automate.Reception()
                            self.Actu()
                            time.sleep(Sec)
                        t1 = time.clock()
                        td = Decimal((t1 - t0))
                        self.Timer(td)
                    if Automate.Ack is True:
                        flag = 0
                        step = 1
                elif step is 1:
                    if self.radioButton_7.isChecked() or self.radioButton_8.isChecked() or self.radioButton_9.isChecked():
                        self.Selec2()
                        NbT = NbT - 1
                        self.label_14.setText(str(NbT) + " points restant")
                        time.sleep(Sec)
                        Mesure.HoldToggle()
                        self.Format()
                        Mesure.STATUS()
                        if Mesure.STATUS() is True:
                            Mesure.HoldToggle()
                            self.Selec2()
                            Automate.Increment_pos(Pas2)
                            Automate.Reception()
                            self.Actu()
                            time.sleep(Sec)
                            self.Timer(td)
                        if Automate.Ack is True:
                            if flag is 1:
                                step = 0
                            else:
                                step = 2
                        self.Selec2()
                    else:
                        Mesure.HoldToggle()
                        self.Format()
                        Mesure.STATUS()
                        if Mesure.STATUS() is True:
                            Mesure.HoldToggle()
                            self.Actu()
                            Automate.Choix_Axe(0)
                            Mesure.Enregistrer_log()
                            self.Text_Aff3("Séquence finie")
                            self.Text_Aff_Clear()
                            step = 3
                elif step is 2:
                    self.Selec1()
                    for x in range(int(Pmax1 * 100), int(Pmin1 * 100), int(-Pas1 * 100)):
                        NbT = NbT - 1
                        self.label_14.setText(str(NbT) + " points restant")
                        Mesure.HoldToggle()
                        self.Format()
                        Mesure.STATUS()
                        if Mesure.STATUS() is True:
                            Mesure.HoldToggle()
                            self.Selec1()
                            Automate.Increment_pos(-Pas1)
                            Automate.Reception()
                            self.Actu()
                            time.sleep(Sec)
                            self.Timer(td)
                    if Automate.Ack is True:
                        flag = 1
                        step = 1
        except:
            self.Text_Aff3("probleme lors de la séquence")
        ################################################################################

    def Actu(self):
        try:
            Automate.Choix_Axe(3)
            Val = Automate.Position_request()
            self.lineEdit_7.setText(str(Val))
            Automate.Choix_Axe(2)
            Val = Automate.Position_request()
            self.lineEdit_8.setText(str(Val))
            Automate.Choix_Axe(1)
            Val = Automate.Position_request()
            self.lineEdit_9.setText(str(Val))
            Automate.Choix_Axe(0)
        except:
            self.Text_Aff3("Erreur dans l'actualisation")

    def Selec(self):
        global axis
        try:
            if self.radioButton.isChecked():
                Automate.Choix_Axe(3)
                axis = 'x'
            if self.radioButton_2.isChecked():
                Automate.Choix_Axe(2)
                axis = 'y'
            if self.radioButton_3.isChecked():
                Automate.Choix_Axe(1)
                axis = 'z'
        except:
            self.Text_Aff3("Erreur choix de l'axe")
        ##################################################################################

        ###########################Function Position######################################

    def Selec1(self):
        global axis1, Val1
        if self.radioButton_4.isChecked():
            Automate.Choix_Axe(3)
            axis1 = 'X'
            Val1 = Automate.Position_request()
            self.lineEdit_7.setText(str(Val1))
        if self.radioButton_5.isChecked():
            Automate.Choix_Axe(2)
            axis1 = 'Y'
            Val1 = Automate.Position_request()
            self.lineEdit_8.setText(str(Val1))
        if self.radioButton_6.isChecked():
            Automate.Choix_Axe(1)
            axis1 = 'Z'
            Val1 = Automate.Position_request()
            self.lineEdit_9.setText(str(Val1))

    def Affich1(self):
        global Pas1, Pmax1, Pmin1, Nb1
        Pmin1 = float(self.lineEdit.text())
        Pmax1 = float(self.lineEdit_2.text())
        Pas1 = float(self.lineEdit_3.text())
        Nb1 = int(((Pmax1 - Pmin1) / Pas1))
        Nb1 = Nb1 + 1
        while Pmin1 <= Pmax1:
            self.Text_AFF1(axis1 + ": " + str(Pmin1))
            Pmin1 = Pmin1 + Pas1
        Pmin1 = float(self.lineEdit.text())
        self.Text_Aff3("Paramètre de position acquise")

    def Selec2(self):
        global axis2, Val2
        if self.radioButton_7.isChecked():
            Automate.Choix_Axe(3)
            axis2 = 'X'
            Val2 = Automate.Position_request()
            self.lineEdit_7.setText(str(Val2))
        if self.radioButton_8.isChecked():
            Automate.Choix_Axe(2)
            axis2 = 'Y'
            Val2 = Automate.Position_request()
            self.lineEdit_8.setText(str(Val2))
        if self.radioButton_9.isChecked():
            Automate.Choix_Axe(1)
            axis2 = 'Z'
            Val2 = Automate.Position_request()
            self.lineEdit_9.setText(str(Val2))

    def Affich2(self):
        global Pas2, Pmin2, Pmax2, Nb2
        if self.radioButton_7.isChecked() or self.radioButton_8.isChecked() or self.radioButton_9.isChecked():
            Pmin2 = float(self.lineEdit_11.text())
            Pmax2 = float(self.lineEdit_12.text())
            Pas2 = float(self.lineEdit_13.text())
            Nb2 = int((Pmax2 - Pmin2) / Pas2)
            Nb2 = Nb2 + 1
            while Pmin2 <= Pmax2:
                self.Text_AFF1(axis2 + ": " + str(Pmin2))
                Pmin2 = Pmin2 + Pas2
            Pmin2 = float(self.lineEdit_11.text())
        self.Text_Aff3("Paramètre de position acquise")
        ##################################################################################

        #################################Function Freq####################################

    def AffichF(self):
        global FreqD, FreqF, PasF
        Mesure.Eregistrer("Freq (Hz);")
        FreqD = float(self.lineEdit_4.text())
        FreqF = float(self.lineEdit_5.text())
        Fnb = float(self.lineEdit_6.text()) - 1
        Mesure.SetFreq()
        Mesure.NBsweepPoint()
        PasF = (FreqF - FreqD) / Fnb
        while FreqD <= FreqF:
            Mesure.Eregistrer(FreqD)
            Mesure.Eregistrer(";")
            self.Text_AFF2(str(FreqD))
            FreqD = FreqD + PasF
        FreqD = float(self.lineEdit_4.text())
        self.Text_Aff3("Paramètre de frequence acquise")
        Mesure.Eregistrer("\n")
        #################################################################################

        ##################################Function Enregitre#############################

    def Parcourir(self):
        global path
        Parcourir.App()
        path = str(Parcourir.fileName)
        self.lineEdit_14.setText(path)
        msg = QMessageBox()
        msg.setWindowTitle("Save")
        msg.setText("voulez vous enregistré dans \n {}".format(path))
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.buttonClicked.connect(self.popup_but)

        x = msg.exec()

    def popup_but(self, i):
        if "No" in i.text():
            self.Parcourir()
        else:
            self.Text_Aff3("La séquence seras enregistré dans {}".format(path))
        #################################################################################

    def Timer(self, td):
        tr = Decimal(td * NbT)
        NbHr = Decimal(tr / 3600)
        NbH = NbHr.quantize(Decimal('1'), rounding=ROUND_HALF_DOWN)
        NbMr = Decimal((tr / 60) - (NbH * 60))
        if NbMr < 1:
            NbM = 0
        else:
            NbM = NbMr.quantize(Decimal('1'), rounding=ROUND_HALF_DOWN)
        NbSr = Decimal(tr - NbM * 60 - NbH * 3600)
        NbS = NbSr.quantize(Decimal('1.01'), rounding=ROUND_HALF_UP)
        self.label_14.setText(str(NbT) + " points restant")
        self.label_15.setText(
            "Temps restant " + str(NbH) + " : " + str(NbM) + " : " + str(NbS) + ' environ')

    def T1(self):
        threading.Thread(target=self.B1).start()

    def T2(self):
        threading.Thread(target=self.B2).start()

    def T3(self):
        threading.Thread(target=self.B3).start()

    def T4(self):
        threading.Thread(target=self.B4).start()

    def T5(self):
        threading.Thread(target=self.B5).start()

    def T6(self):
        threading.Thread(target=self.B6).start()

    def T7(self):
        threading.Thread(target=self.B7).start()

    def T8(self):
        threading.Thread(target=self.B8).start()

    def T9(self):
        threading.Thread(target=self.B9).start()

    def T10(self):
        threading.Thread(target=self.B10).start()

    def T11(self):
        threading.Thread(target=self.B11).start()

    def T13(self):
        threading.Thread(target=self.B13).start()

    def T14(self):
        threading.Thread(target=self.B14).start()

    def T15(self):
        threading.Thread(target=self.B15).start()

    def T16(self):
        threading.Thread(target=self.AffichF).start()

    def T17(self):
        threading.Thread(target=self.B17).start()

    def T19(self):
        threading.Thread(target=self.B19).start()
