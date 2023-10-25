# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notifyspace.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Ui.images_rc

class Ui_NotifySpace(object):
    def setupUi(self, NotifySpace):
        if not NotifySpace.objectName():
            NotifySpace.setObjectName(u"NotifySpace")
        NotifySpace.resize(300, 233)
        NotifySpace.setMinimumSize(QSize(300, 0))
        NotifySpace.setMaximumSize(QSize(300, 16777215))
        NotifySpace.setStyleSheet(u"border: 1px solid rgb(50, 50, 50);")
        self.verticalLayout = QVBoxLayout(NotifySpace)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.notify_space_layout = QVBoxLayout()
        self.notify_space_layout.setSpacing(3)
        self.notify_space_layout.setObjectName(u"notify_space_layout")
        self.notify_space_layout.setContentsMargins(0, 0, -1, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.notify_space_layout.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.notify_space_layout)


        self.retranslateUi(NotifySpace)

        QMetaObject.connectSlotsByName(NotifySpace)
    # setupUi

    def retranslateUi(self, NotifySpace):
        NotifySpace.setWindowTitle(QCoreApplication.translate("NotifySpace", u"Form", None))
    # retranslateUi

