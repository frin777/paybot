# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileeditor.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
import Ui.images_rc

class Ui_ProfileEditror(object):
    def setupUi(self, ProfileEditror):
        if not ProfileEditror.objectName():
            ProfileEditror.setObjectName(u"ProfileEditror")
        ProfileEditror.resize(700, 395)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileEditror.sizePolicy().hasHeightForWidth())
        ProfileEditror.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ProfileEditror)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headwidget = QWidget(ProfileEditror)
        self.headwidget.setObjectName(u"headwidget")
        self.headwidget.setMinimumSize(QSize(0, 30))
        self.headwidget.setMaximumSize(QSize(16777215, 30))
        self.headwidget.setStyleSheet(u"background-color: rgb(30, 31, 34);\n"
"border-top-left-radius: 3px;\n"
"border-top-right-radius: 3px;")
        self.horizontalLayout = QHBoxLayout(self.headwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.label_3 = QLabel(self.headwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/img/icon20.png"))

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.label = QLabel(self.headwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(12)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(208, 208, 208);")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QToolButton(self.headwidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/img/\u0445.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.headwidget)

        self.body_widget = QWidget(ProfileEditror)
        self.body_widget.setObjectName(u"body_widget")
        self.body_widget.setStyleSheet(u"background-color: rgb(43, 45, 49);")
        self.verticalLayout_3 = QVBoxLayout(self.body_widget)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 3)

        self.verticalLayout.addWidget(self.body_widget)


        self.retranslateUi(ProfileEditror)

        QMetaObject.connectSlotsByName(ProfileEditror)
    # setupUi

    def retranslateUi(self, ProfileEditror):
        ProfileEditror.setWindowTitle(QCoreApplication.translate("ProfileEditror", u"Form", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("ProfileEditror", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.close_btn.setText(QCoreApplication.translate("ProfileEditror", u"...", None))
    # retranslateUi

