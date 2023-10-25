# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'useritem.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_UserItemForm(object):
    def setupUi(self, UserItemForm):
        if not UserItemForm.objectName():
            UserItemForm.setObjectName(u"UserItemForm")
        UserItemForm.resize(656, 32)
        UserItemForm.setMinimumSize(QSize(0, 0))
        UserItemForm.setMaximumSize(QSize(16777215, 32))
        UserItemForm.setStyleSheet(u"QWidget {\n"
"    border: 1px solid rgba(65, 65, 65, 100);\n"
"    border-radius: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(44, 44, 44, 100);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(UserItemForm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.nick_label = QLabel(UserItemForm)
        self.nick_label.setObjectName(u"nick_label")
        self.nick_label.setMaximumSize(QSize(16777215, 32))
        self.nick_label.setStyleSheet(u"QLabel {\n"
"border-right: 0px;\n"
"padding-left: 3px;\n"
"}")

        self.horizontalLayout.addWidget(self.nick_label)

        self.card_number_label = QLineEdit(UserItemForm)
        self.card_number_label.setObjectName(u"card_number_label")
        self.card_number_label.setEnabled(True)
        self.card_number_label.setMinimumSize(QSize(0, 0))
        self.card_number_label.setMaximumSize(QSize(250, 32))
        self.card_number_label.setStyleSheet(u"QLineEdit {\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"}")
        self.card_number_label.setReadOnly(True)

        self.horizontalLayout.addWidget(self.card_number_label)

        self.bank_name_label = QLabel(UserItemForm)
        self.bank_name_label.setObjectName(u"bank_name_label")
        self.bank_name_label.setMinimumSize(QSize(0, 32))
        self.bank_name_label.setMaximumSize(QSize(16777215, 32))
        self.bank_name_label.setStyleSheet(u"QLabel {\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"}")

        self.horizontalLayout.addWidget(self.bank_name_label)

        self.balance_label = QLabel(UserItemForm)
        self.balance_label.setObjectName(u"balance_label")
        self.balance_label.setMaximumSize(QSize(16777215, 32))
        self.balance_label.setStyleSheet(u"border-left: 0px;\n"
"border-right: 0px;")

        self.horizontalLayout.addWidget(self.balance_label)

        self.pushButton = QPushButton(UserItemForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(70, 32))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	background-color: rgba(0, 53, 80, 100);\n"
"	color: rgb(185, 185, 185);\n"
"	border-left: 0px;\n"
"	height: 30px;\n"
"	font: 900 10pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.0341364, x2:1, y2:1, stop:0 rgba(0, 0, 0, 66), stop:1 rgba(37, 33, 33, 255));\n"
"	color: rgb(162, 162, 69);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"		\n"
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid #888;\n"
"    }")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(UserItemForm)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(70, 32))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"  	\n"
"	\n"
"	background-color: rgba(70, 0, 0, 100);\n"
"	color: rgb(185, 185, 185);\n"
"	border-left: 0px;\n"
"	height: 30px;\n"
"	font: 900 10pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.0341364, x2:1, y2:1, stop:0 rgba(0, 0, 0, 66), stop:1 rgba(37, 33, 33, 255));\n"
"	color: rgb(162, 162, 69);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled {\n"
"        \n"
"		\n"
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid #888;\n"
"    }")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(UserItemForm)

        QMetaObject.connectSlotsByName(UserItemForm)
    # setupUi

    def retranslateUi(self, UserItemForm):
        UserItemForm.setWindowTitle(QCoreApplication.translate("UserItemForm", u"Form", None))
        self.nick_label.setText(QCoreApplication.translate("UserItemForm", u"Nickname", None))
        self.card_number_label.setText(QCoreApplication.translate("UserItemForm", u"CardNumber", None))
        self.bank_name_label.setText(QCoreApplication.translate("UserItemForm", u"Bank", None))
        self.balance_label.setText(QCoreApplication.translate("UserItemForm", u"Balance", None))
        self.pushButton.setText(QCoreApplication.translate("UserItemForm", u"\u041e\u043f\u043b\u0430\u0447\u0435\u043d", None))
        self.pushButton_2.setText(QCoreApplication.translate("UserItemForm", u"\u0411\u0430\u043d", None))
    # retranslateUi

