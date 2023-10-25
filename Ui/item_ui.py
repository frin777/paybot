# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(608, 30)
        Form.setMinimumSize(QSize(0, 30))
        Form.setMaximumSize(QSize(16777215, 30))
        Form.setStyleSheet(u"QWidget {\n"
"    border: 1px solid rgba(65, 65, 65, 100);\n"
"    border-radius: 1px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(44, 44, 44, 100);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"border-right: 0px;\n"
"padding-left: 3px;\n"
"}")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"border-left: 0px;\n"
"border-right: 0px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_3)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 20))
        self.pushButton.setMaximumSize(QSize(70, 50))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
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
"        border: 0px solid #888;\n"
"    }")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

