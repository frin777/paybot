# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nitify.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)
import Ui.images_rc

class Ui_Notify(object):
    def setupUi(self, Notify):
        if not Notify.objectName():
            Notify.setObjectName(u"Notify")
        Notify.resize(300, 36)
        Notify.setMinimumSize(QSize(300, 36))
        Notify.setMaximumSize(QSize(300, 36))
        self.horizontalLayout_2 = QHBoxLayout(Notify)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(Notify)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(36, 36, 37, 222);\n"
"	color: rgb(185, 185, 185);\n"
"	border: 1px solid rgb(45, 45, 45);\n"
"	border-width: 1px;\n"
"	border-radius: 2px;\n"
"	padding-left: 4px;\n"
"	padding-right: 2px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 15))
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet(u"border-width: 0px;\n"
"background-color: rgba(36, 36, 37, 0);")
        self.label.setPixmap(QPixmap(u":/img/444.png"))

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setStyleSheet(u"border-width: 0px;\n"
"background-color: rgba(36, 36, 37, 0);\n"
"padding-bottom:2px;")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Notify)

        QMetaObject.connectSlotsByName(Notify)
    # setupUi

    def retranslateUi(self, Notify):
        Notify.setWindowTitle(QCoreApplication.translate("Notify", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Notify", u"Notification", None))
    # retranslateUi

