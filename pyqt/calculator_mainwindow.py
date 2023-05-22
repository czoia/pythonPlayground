# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect,
                            QSize)
from PySide6.QtWidgets import (QHBoxLayout, QLineEdit,
                               QPushButton, QVBoxLayout, QWidget)


class Calculator_MainWindow(object):
    # square radix char encoding
    SQUARE_RADIX_CHAR = '\u221a'
    # plus/minus char encoding
    PLUS_MINUS_CHAR = "\u00b1"
    # go-back arrow char encoding
    ROLLBACK_CHAR = "\u21a9"

    def __init__(self):
        self.map_buttons = {
            "A/C": None, self.PLUS_MINUS_CHAR: None, "%": None,
            self.ROLLBACK_CHAR: None, "(": None,
            "7": None, "8": None, "9": None, "/": None, ")": None,
            "4": None, "5": None, "6": None, "*": None, "^": None,
            "1": None, "2": None, "3": None, "-": None, self.SQUARE_RADIX_CHAR: None,
            "0": None, ",": None, "+": None, "=": None}

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 310)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inputLine = QLineEdit(self.centralwidget)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setGeometry(QRect(10, 10, 791, 41))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 69, 781, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"ac_button")
        self.pushButton_2.setMinimumSize(QSize(50, 27))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["A/C"] = self.pushButton_2

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_30 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(50, 27))
        self.pushButton_30.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons[self.PLUS_MINUS_CHAR] = self.pushButton_30

        self.horizontalLayout.addWidget(self.pushButton_30)

        self.pushButton_29 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(50, 27))
        self.pushButton_29.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["%"] = self.pushButton_29

        self.horizontalLayout.addWidget(self.pushButton_29)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 27))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons[self.ROLLBACK_CHAR] = self.pushButton_4

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 27))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["("] = self.pushButton_3

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_25 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(50, 27))
        self.pushButton_25.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["7"] = self.pushButton_25

        self.horizontalLayout_7.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(50, 27))
        self.pushButton_26.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["8"] = self.pushButton_26

        self.horizontalLayout_7.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(50, 27))
        self.pushButton_27.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["9"] = self.pushButton_27

        self.horizontalLayout_7.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(50, 27))
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["/"] = self.pushButton_28

        self.horizontalLayout_7.addWidget(self.pushButton_28)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 27))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons[")"] = self.pushButton
        
        self.horizontalLayout_7.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_21 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(50, 27))
        self.pushButton_21.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["4"] = self.pushButton_21

        self.horizontalLayout_6.addWidget(self.pushButton_21)

        self.pushButton_34 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(50, 27))
        self.pushButton_34.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["5"] = self.pushButton_34

        self.horizontalLayout_6.addWidget(self.pushButton_34)

        self.pushButton_33 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(50, 27))
        self.pushButton_33.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["6"] = self.pushButton_33

        self.horizontalLayout_6.addWidget(self.pushButton_33)

        self.pushButton_22 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(50, 27))
        self.pushButton_22.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["*"] = self.pushButton_22

        self.horizontalLayout_6.addWidget(self.pushButton_22)

        self.pushButton_31 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(50, 27))
        self.pushButton_31.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["^"] = self.pushButton_31

        self.horizontalLayout_6.addWidget(self.pushButton_31)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_20 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(50, 27))
        self.pushButton_20.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["1"] = self.pushButton_20

        self.horizontalLayout_8.addWidget(self.pushButton_20)

        self.pushButton_37 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(50, 27))
        self.pushButton_37.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["2"] = self.pushButton_37

        self.horizontalLayout_8.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(50, 27))
        self.pushButton_38.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["3"] = self.pushButton_38

        self.horizontalLayout_8.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(50, 27))
        self.pushButton_39.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["-"] = self.pushButton_39

        self.horizontalLayout_8.addWidget(self.pushButton_39)

        self.pushButton_32 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(50, 27))
        self.pushButton_32.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons[self.SQUARE_RADIX_CHAR] = self.pushButton_32

        self.horizontalLayout_8.addWidget(self.pushButton_32)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_17 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(50, 27))
        self.pushButton_17.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_17.setBaseSize(QSize(0, 0))
        self.map_buttons["0"] = self.pushButton_17

        self.horizontalLayout_5.addWidget(self.pushButton_17)

        self.pushButton_19 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(50, 27))
        self.pushButton_19.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_19.setBaseSize(QSize(0, 0))
        self.map_buttons[","] = self.pushButton_19

        self.horizontalLayout_5.addWidget(self.pushButton_19)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(50, 27))
        self.pushButton_18.setMaximumSize(QSize(16777215, 16777215))
        self.map_buttons["+"] = self.pushButton_18

        self.horizontalLayout_5.addWidget(self.pushButton_18)

        self.equal_button = QPushButton(self.verticalLayoutWidget)
        self.equal_button.setObjectName(u"equal_button")
        self.equal_button.setMinimumSize(QSize(100, 27))
        self.equal_button.setMaximumSize(QSize(16777215, 16777215))
        self.equal_button.setAutoFillBackground(False)
        self.equal_button.setStyleSheet(u"background-color: rgb(115, 210, 22);")
        self.map_buttons["="] = self.equal_button

        self.horizontalLayout_5.addWidget(self.equal_button)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyQtCalculator", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"A/C", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u21a9", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.equal_button.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi
