# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../QtProject\mainwindow.ui'
#
# Created: Tue Mar  3 00:05:19 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.startCycle = QtGui.QPushButton(self.centralWidget)
        self.startCycle.setGeometry(QtCore.QRect(70, 610, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startCycle.setFont(font)
        self.startCycle.setObjectName("startCycle")
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(
            QtCore.QRect(580, 20, 285, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.chronometerLabel = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(50)
        font.setBold(False)
        self.chronometerLabel.setFont(font)
        self.chronometerLabel.setObjectName("chronometerLabel")
        self.horizontalLayout_3.addWidget(self.chronometerLabel)
        self.startChrono = QtGui.QPushButton(self.centralWidget)
        self.startChrono.setGeometry(QtCore.QRect(980, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startChrono.setFont(font)
        self.startChrono.setObjectName("startChrono")
        self.pauseChrono = QtGui.QPushButton(self.centralWidget)
        self.pauseChrono.setGeometry(QtCore.QRect(1060, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pauseChrono.setFont(font)
        self.pauseChrono.setObjectName("pauseChrono")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(960, 360, 351, 201))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtGui.QScrollArea(self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 331, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 329, 169))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.consoleBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.consoleBrowser.setGeometry(QtCore.QRect(0, 0, 331, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(158, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(158, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.consoleBrowser.setPalette(palette)
        self.consoleBrowser.setObjectName("consoleBrowser")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.clearConsole = QtGui.QPushButton(self.centralWidget)
        self.clearConsole.setGeometry(QtCore.QRect(1060, 590, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clearConsole.setFont(font)
        self.clearConsole.setObjectName("clearConsole")
        self.restartChrono = QtGui.QPushButton(self.centralWidget)
        self.restartChrono.setGeometry(QtCore.QRect(1140, 20, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.restartChrono.setFont(font)
        self.restartChrono.setObjectName("restartChrono")
        self.flag_structure_label = QtGui.QLabel(self.centralWidget)
        self.flag_structure_label.setGeometry(QtCore.QRect(550, 320, 341, 341))
        self.flag_structure_label.setText("")
        self.flag_structure_label.setTextFormat(QtCore.Qt.AutoText)
        self.flag_structure_label.setPixmap(
            QtGui.QPixmap(":/resources/flag_structure.png"))
        self.flag_structure_label.setScaledContents(True)
        self.flag_structure_label.setIndent(-1)
        self.flag_structure_label.setObjectName("flag_structure_label")
        self.square_0_label = QtGui.QLabel(self.centralWidget)
        self.square_0_label.setGeometry(QtCore.QRect(563, 335, 100, 100))
        self.square_0_label.setText("")
        self.square_0_label.setScaledContents(True)
        self.square_0_label.setIndent(-1)
        self.square_0_label.setObjectName("square_0_label")
        self.square_1_label = QtGui.QLabel(self.centralWidget)
        self.square_1_label.setGeometry(QtCore.QRect(674, 337, 95, 95))
        self.square_1_label.setText("")
        self.square_1_label.setScaledContents(True)
        self.square_1_label.setIndent(-1)
        self.square_1_label.setObjectName("square_1_label")
        self.square_2_label = QtGui.QLabel(self.centralWidget)
        self.square_2_label.setGeometry(QtCore.QRect(780, 333, 100, 100))
        self.square_2_label.setText("")
        self.square_2_label.setScaledContents(True)
        self.square_2_label.setIndent(-1)
        self.square_2_label.setObjectName("square_2_label")
        self.square_3_label = QtGui.QLabel(self.centralWidget)
        self.square_3_label.setGeometry(QtCore.QRect(562, 444, 100, 100))
        self.square_3_label.setText("")
        self.square_3_label.setScaledContents(True)
        self.square_3_label.setIndent(-1)
        self.square_3_label.setObjectName("square_3_label")
        self.square_4_label = QtGui.QLabel(self.centralWidget)
        self.square_4_label.setGeometry(QtCore.QRect(671, 442, 100, 100))
        self.square_4_label.setText("")
        self.square_4_label.setScaledContents(True)
        self.square_4_label.setIndent(-1)
        self.square_4_label.setObjectName("square_4_label")
        self.square_5_label = QtGui.QLabel(self.centralWidget)
        self.square_5_label.setGeometry(QtCore.QRect(779, 442, 100, 100))
        self.square_5_label.setText("")
        self.square_5_label.setScaledContents(True)
        self.square_5_label.setIndent(-1)
        self.square_5_label.setObjectName("square_5_label")
        self.square_6_label = QtGui.QLabel(self.centralWidget)
        self.square_6_label.setGeometry(QtCore.QRect(562, 550, 100, 100))
        self.square_6_label.setText("")
        self.square_6_label.setScaledContents(True)
        self.square_6_label.setIndent(-1)
        self.square_6_label.setObjectName("square_6_label")
        self.square_7_label = QtGui.QLabel(self.centralWidget)
        self.square_7_label.setGeometry(QtCore.QRect(672, 550, 100, 100))
        self.square_7_label.setText("")
        self.square_7_label.setScaledContents(True)
        self.square_7_label.setIndent(-1)
        self.square_7_label.setObjectName("square_7_label")
        self.square_8_label = QtGui.QLabel(self.centralWidget)
        self.square_8_label.setGeometry(QtCore.QRect(779, 549, 100, 100))
        self.square_8_label.setText("")
        self.square_8_label.setScaledContents(True)
        self.square_8_label.setIndent(-1)
        self.square_8_label.setObjectName("square_8_label")
        self.countryLabel = QtGui.QLabel(self.centralWidget)
        self.countryLabel.setGeometry(QtCore.QRect(650, 220, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setWeight(50)
        font.setBold(False)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(550, 220, 91, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(550, 140, 147, 39))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.questionLabel = QtGui.QLabel(self.centralWidget)
        self.questionLabel.setGeometry(QtCore.QRect(700, 140, 611, 39))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(50)
        font.setBold(False)
        self.questionLabel.setFont(font)
        self.questionLabel.setObjectName("questionLabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "Atlas", None, QtGui.QApplication.UnicodeUTF8))
        self.startCycle.setText(QtGui.QApplication.translate(
            "MainWindow", "Démarrer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate(
            "MainWindow", "Chronographe : ", None, QtGui.QApplication.UnicodeUTF8))
        self.chronometerLabel.setText(QtGui.QApplication.translate(
            "MainWindow", "Nope", None, QtGui.QApplication.UnicodeUTF8))
        self.startChrono.setText(QtGui.QApplication.translate(
            "MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pauseChrono.setText(QtGui.QApplication.translate(
            "MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate(
            "MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.consoleBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                 "p, li { white-space: pre-wrap; }\n"
                                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearConsole.setText(QtGui.QApplication.translate(
            "MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.restartChrono.setText(QtGui.QApplication.translate(
            "MainWindow", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.countryLabel.setText(QtGui.QApplication.translate(
            "MainWindow", "Nope", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate(
            "MainWindow", "Pays :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate(
            "MainWindow", "Question : ", None, QtGui.QApplication.UnicodeUTF8))
        self.questionLabel.setText(QtGui.QApplication.translate(
            "MainWindow", "Nope", None, QtGui.QApplication.UnicodeUTF8))

import BaseStation.ui.QtProject.GeneratedFiles.resources_rc
