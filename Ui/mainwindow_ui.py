# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)
import Ui.images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1003, 733)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headwidget = QWidget(self.centralwidget)
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
        self.label = QLabel(self.headwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Showcard Gothic"])
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(208, 208, 208);")
        self.label.setPixmap(QPixmap(u":/img/icon20.png"))

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimize_btn = QToolButton(self.headwidget)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/img/_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.minimize_btn)

        self.close_btn = QToolButton(self.headwidget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/img/\u0445.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.headwidget)

        self.body_widget = QWidget(self.centralwidget)
        self.body_widget.setObjectName(u"body_widget")
        self.body_widget.setStyleSheet(u"background-color: rgb(43, 45, 49);")
        self.verticalLayout_3 = QVBoxLayout(self.body_widget)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.index_page_btn = QPushButton(self.body_widget)
        self.index_page_btn.setObjectName(u"index_page_btn")
        self.index_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.index_page_btn.setFocusPolicy(Qt.NoFocus)
        self.index_page_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border: 1px solid rgba(65, 65, 65, 100);\n"
"	border-radius: 1px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid rgba(100, 100, 100, 100);\n"
"    }")

        self.verticalLayout_2.addWidget(self.index_page_btn)

        self.settings_page_btn = QPushButton(self.body_widget)
        self.settings_page_btn.setObjectName(u"settings_page_btn")
        self.settings_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings_page_btn.setFocusPolicy(Qt.NoFocus)
        self.settings_page_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border: 1px solid rgba(65, 65, 65, 100);\n"
"	border-radius: 1px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid rgba(100, 100, 100, 100);\n"
"    }")

        self.verticalLayout_2.addWidget(self.settings_page_btn)

        self.stat_page_btn = QPushButton(self.body_widget)
        self.stat_page_btn.setObjectName(u"stat_page_btn")
        self.stat_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stat_page_btn.setFocusPolicy(Qt.NoFocus)
        self.stat_page_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border: 1px solid rgba(65, 65, 65, 100);\n"
"	border-radius: 1px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid rgba(100, 100, 100, 100);\n"
"    }")

        self.verticalLayout_2.addWidget(self.stat_page_btn)

        self.payment_page_btn = QPushButton(self.body_widget)
        self.payment_page_btn.setObjectName(u"payment_page_btn")
        self.payment_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.payment_page_btn.setFocusPolicy(Qt.NoFocus)
        self.payment_page_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border: 1px solid rgba(65, 65, 65, 100);\n"
"	border-radius: 1px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid rgba(100, 100, 100, 100);\n"
"    }")

        self.verticalLayout_2.addWidget(self.payment_page_btn)

        self.users_page_btn = QPushButton(self.body_widget)
        self.users_page_btn.setObjectName(u"users_page_btn")
        self.users_page_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.users_page_btn.setFocusPolicy(Qt.NoFocus)
        self.users_page_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border: 1px solid rgba(65, 65, 65, 100);\n"
"	border-radius: 1px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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
"		background-color: rgb(50, 50, 50);\n"
"        color: #888;\n"
"        border: 1px solid rgba(100, 100, 100, 100);\n"
"    }")

        self.verticalLayout_2.addWidget(self.users_page_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget = QTabWidget(self.body_widget)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(9)
        self.tabWidget.setFont(font1)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"border: 1px solid rgb(72, 72, 72);\n"
"border-top: 0px;\n"
"border-right: 0px;\n"
"border-bottom: 0px;\n"
"background: rgb(245, 245, 245);;\n"
"}\n"
"\n"
"QTabBar::tab { height: 0; width: 0; margin: 0; padding: 0; }\n"
"\n"
"QTabBar::tab:selected {\n"
"background: rgb(50, 50, 50);\n"
"margin-bottom: -1px;\n"
"font: 900 9pt \"Segoe UI Black\";\n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.index_page = QWidget()
        self.index_page.setObjectName(u"index_page")
        self.verticalLayout_5 = QVBoxLayout(self.index_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.page_name_index = QLabel(self.index_page)
        self.page_name_index.setObjectName(u"page_name_index")
        font2 = QFont()
        font2.setPointSize(14)
        self.page_name_index.setFont(font2)
        self.page_name_index.setStyleSheet(u"color: rgb(170, 255, 0);")

        self.verticalLayout_5.addWidget(self.page_name_index)

        self.line_2 = QFrame(self.index_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.textBrowser = QTextBrowser(self.index_page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	\n"
"	color: rgb(191, 191, 95);\n"
"	border: 0px solid rgb(72, 72, 72);\n"
"	padding-left: 5px;\n"
"	max-height: 120px;\n"
"	min-height: 120px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"border: 0px solid rgb(72, 72, 72);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: yellow;    /* #2A2929; */\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: blue;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
" "
                        "   {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:ho"
                        "rizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        \n"
"		background-color: rgb(88, 88, 88);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        sub"
                        "control-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")

        self.verticalLayout_5.addWidget(self.textBrowser)

        self.verticalSpacer_3 = QSpacerItem(20, 347, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.index_page, "")
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_7 = QVBoxLayout(self.settings_page)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.settings_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMouseTracking(False)
        self.groupBox.setToolTipDuration(-1)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius: 6px;\n"
"    margin-top:10px;\n"
" \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 71px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(110, 163, 81);")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet(u"/* \u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u0431\u043e\u043a\u0441  */\n"
"QComboBox {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 8px 18px 8px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"/* \u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a  */\n"
"QComboBox QAbstractItemView {\n"
"     border: 4px solid rgb(45, 45, 45);\n"
"     color: rgb(208, 208, 208);\n"
" }\n"
"\n"
"QComboBox:editable {\n"
"    background-color: rgb(163, 163, 163);\n"
"    color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background-color: rgb(36, 36, 37);\n"
"\n"
"}\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background-color: rgb(36, 36, 37);\n"
"	color: rgb(208, 208, 208);\n"
"padding: 8px 18px 8px 10px;\n"
"}\n"
"\n"
"QComboBox:on { /* shift"
                        " the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0441\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::drop-down {\n"
"    width: 15px;\n"
"	padding-right:5px;\n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0441\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/img/444.png)\n"
"}\n"
" /* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::down-arrow:on {\n"
"	image: url(:/img/555.png);\n"
"}")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(110, 163, 81);")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"/* \u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u0431\u043e\u043a\u0441  */\n"
"QComboBox {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 8px 18px 8px 10px;\n"
"    min-width: 6em;\n"
"    color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"/* \u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a  */\n"
"QComboBox QAbstractItemView {\n"
"     border: 4px solid rgb(45, 45, 45);\n"
"     color: rgb(208, 208, 208);\n"
" }\n"
"\n"
"QComboBox:editable {\n"
"    background-color: rgb(163, 163, 163);\n"
"    color: rgb(208, 208, 208);\n"
"}\n"
"\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background-color: rgb(36, 36, 37);\n"
"\n"
"}\n"
"\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background-color: rgb(36, 36, 37);\n"
"	color: rgb(208, 208, 208);\n"
"padding: 8px 18px 8px 10px;\n"
"}\n"
"\n"
"QComboBox:on { /* shift"
                        " the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0441\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::drop-down {\n"
"    width: 15px;\n"
"	padding-right:5px;\n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"\n"
"/* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0441\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::down-arrow {\n"
"    image: url(:/img/444.png)\n"
"}\n"
" /* \u0421\u0442\u0440\u0435\u043b\u043a\u0430 \u0440\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0433\u043e \u043c\u0435\u043d\u044e */\n"
"QComboBox::down-arrow:on {\n"
"	image: url(:/img/555.png);\n"
"}")

        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(167, 16777215))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(50, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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

        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.settings_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius: 6px;\n"
"    margin-top:10px;\n"
" \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 71px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(1)
        self.gridLayout_2.setVerticalSpacing(5)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(110, 163, 81);")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(167, 16777215))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(50, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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

        self.gridLayout_2.addWidget(self.pushButton_2, 3, 3, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(669, 16777215))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 3)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(216, 216, 216);")

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 4)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(216, 216, 216);")
        self.label_6.setLineWidth(1)
        self.label_6.setScaledContents(False)
        self.label_6.setIndent(-1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(216, 216, 216);")

        self.gridLayout_2.addWidget(self.label_8, 0, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.settings_page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius: 6px;\n"
"    margin-top:10px;\n"
" \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 71px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(110, 163, 81);")

        self.verticalLayout_6.addWidget(self.label_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(669, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"}")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(167, 16777215))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(50, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(110, 163, 81);")

        self.verticalLayout_10.addWidget(self.label_9)

        self.textEdit = QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"}")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.pushButton_5 = QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 5px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(50, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 23px;\n"
"	min-width: 100px;\n"
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

        self.verticalLayout_10.addWidget(self.pushButton_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.tabWidget.addTab(self.settings_page, "")
        self.stat_page = QWidget()
        self.stat_page.setObjectName(u"stat_page")
        self.verticalLayout_8 = QVBoxLayout(self.stat_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.stat_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"color: rgb(185, 185, 185);\n"
"font: 900 10pt \"Segoe UI Black\";")
        self.verticalLayout_11 = QVBoxLayout(self.widget_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        self.label_11.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.tabWidget.addTab(self.stat_page, "")
        self.payment_page = QWidget()
        self.payment_page.setObjectName(u"payment_page")
        self.verticalLayout_9 = QVBoxLayout(self.payment_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit_3 = QLineEdit(self.payment_page)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.line_5 = QFrame(self.payment_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.widget = QWidget(self.payment_page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit_4)

        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.horizontalLayout_6.addWidget(self.lineEdit_5)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton\n"
"{\n"
"  	background-color: rgb(36, 36, 37);\n"
"	color: rgb(185, 185, 185);\n"
"    padding: 2px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(50, 50, 50);\n"
"	border-radius: 2px;\n"
"	height: 30px;\n"
"	min-width: 100px;\n"
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

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_9.addWidget(self.widget)

        self.listWidget = QListWidget(self.payment_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QScrollArea {\n"
"border: 0px solid rgb(72, 72, 72);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: yellow;    /* #2A2929; */\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: blue;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        sub"
                        "control-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
" "
                        "       width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        \n"
"		background-color: rgb(88, 88, 88);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        "
                        "border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"QListWidget {\n"
"border: 0px;\n"
"}")
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setSpacing(1)
        self.listWidget.setGridSize(QSize(0, 33))
        self.listWidget.setSortingEnabled(False)

        self.verticalLayout_9.addWidget(self.listWidget)

        self.tabWidget.addTab(self.payment_page, "")
        self.users_page = QWidget()
        self.users_page.setObjectName(u"users_page")
        self.verticalLayout_4 = QVBoxLayout(self.users_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit_7 = QLineEdit(self.users_page)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"    border-radius: 3px;\n"
"	margin-top:1px;\n"
"	margin-bottom:3px;\n"
"    padding: 8 8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(56, 58, 64);\n"
"	selection-background-color: rgb(111, 165, 82);\n"
"	font: 900 9pt \"Segoe UI Black\";\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit_7)

        self.line_3 = QFrame(self.users_page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.UsersListWidget = QListWidget(self.users_page)
        self.UsersListWidget.setObjectName(u"UsersListWidget")
        self.UsersListWidget.setStyleSheet(u"QListWidget { border: 0px; }\n"
"QListView::item { height: 32px; }\n"
"\n"
"\n"
"QScrollArea {\n"
"border: 0px solid rgb(72, 72, 72);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: yellow;    /* #2A2929; */\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: blue;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_"
                        "disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
""
                        "    QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        \n"
"		background-color: rgb(88, 88, 88);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::s"
                        "ub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")

        self.verticalLayout_4.addWidget(self.UsersListWidget)

        self.line_6 = QFrame(self.users_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.tabWidget.addTab(self.users_page, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.log_browser = QTextBrowser(self.body_widget)
        self.log_browser.setObjectName(u"log_browser")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.log_browser.setFont(font5)
        self.log_browser.setStyleSheet(u"QTextBrowser {\n"
"	color: rgb(170, 255, 0);\n"
"	border: 1px solid rgb(72, 72, 72);\n"
"	padding-left: 5px;\n"
"	max-height: 120px;\n"
"	min-height: 120px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"border: 0px solid rgb(72, 72, 72);\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"    {\n"
"        height: 15px;\n"
"        margin: 3px 15px 3px 15px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"        background-color: yellow;    /* #2A2929; */\n"
"    }\n"
"\n"
"    QScrollBar::handle:horizontal\n"
"    {\n"
"        background-color: blue;      /* #605F5F; */\n"
"        min-width: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal\n"
"    {\n"
"        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"        width: 10px;\n"
"        height: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:horizontal\n"
"    {\n"
""
                        "        margin: 0px 3px 0px 3px;\n"
"        border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: right;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: left;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"\n"
"    QScrollBar::add-page:horizontal,"
                        " QScrollBar::sub-page:horizontal\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar:vertical\n"
"    {\n"
"        background-color: #2A2929;\n"
"        width: 15px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border: 1px transparent #2A2929;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::handle:vertical\n"
"    {\n"
"        \n"
"		background-color: rgb(88, 88, 88);\n"
"        min-height: 5px;\n"
"        border-radius: 4px;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-p"
                        "osition: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")

        self.verticalLayout_3.addWidget(self.log_browser)


        self.verticalLayout.addWidget(self.body_widget)

        self.footerwidget = QWidget(self.centralwidget)
        self.footerwidget.setObjectName(u"footerwidget")
        self.footerwidget.setMinimumSize(QSize(0, 40))
        self.footerwidget.setMaximumSize(QSize(16777215, 40))
        self.footerwidget.setStyleSheet(u"background-color: rgb(30, 31, 34);\n"
"border-bottom-left-radius: 3px;\n"
"border-bottom-right-radius: 3px;")
        self.horizontalLayout_2 = QHBoxLayout(self.footerwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(115, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.footerwidget)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamilies([u"Showcard Gothic"])
        font6.setPointSize(14)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(193, 151, 0);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(114, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.footerwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)
        self.listWidget.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.minimize_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.index_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.settings_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.stat_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.payment_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u044b", None))
        self.users_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.page_name_index.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u043e\u0441\u0442\u0438", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d \u0432\u044b\u0432\u043e\u0434 \u043d\u043e\u0432\u043e\u0441\u0442\u0435\u0439</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u044f \u043d\u0430 \u0440\u0430\u0431"
                        "\u043e\u0447\u0438\u0439 \u0441\u0442\u043e\u043b, \u043f\u043e\u043a\u0430 \u0447\u0442\u043e \u043d\u0435 \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d\u044b \u0432 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u043e \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430\u043c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u0439</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* \u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0430 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f/\u043e\u0442\u043c\u0435\u043d\u0435\u043d\u0438\u044f \u0437\u0430\u044f\u0432\u043e\u043a \u0447\u0435\u0440\u0435\u0434 \u0434\u0438\u0441\u043a\u043e\u0440\u0434</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.index_page), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u044f \u0434\u043b\u044f \u0440\u0430\u0431\u043e\u0447\u0435\u0433\u043e \u0441\u0442\u043e\u043b\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043d\u0438\u0442\u043e\u0440", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"bottom-right", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"top-right", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"left-top", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"left-bottom", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447 \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RT_jSidC9viIgmuLSFbud4wXk0h7xUBNqyNvAdszQSsMZPyvE", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043a\u043b\u044e\u0447:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c 31 \u0434\u0435\u043d\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0431\u043e\u0442\u0430 Discord", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"API Token", None))
        self.lineEdit_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0431\u043e\u0442\u0430", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043c\u043c\u0430\u043d\u0434:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/help - \u043f\u043e\u043c\u043e\u0449\u044c</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/setpayment &lt;numb"
                        "er&gt; - \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443 \u0434\u043b\u044f \u043e\u043f\u043b\u0430\u0442</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/pay &lt;summ&gt; &lt;desc&gt; - \u0437\u0430\u043f\u0440\u043e\u0441\u0438\u0442\u044c \u043e\u043f\u043b\u0430\u0442\u0443</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/about - \u0418\u0444\u043d\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043c\u043e\u0435\u043c \u0441\u0447\u0435\u0442\u0435</p></body></html>", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_page), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u043f\u043b\u0430\u0447\u0435\u043d\u043e: 2333 \u0440\u0443\u0431", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439: 5", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432: 23", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stat_page), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0438\u043a\u0443", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Senbry", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"20 key x 2", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.payment_page), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0440\u043e\u0441\u044b \u043d\u0430 \u0432\u044b\u043f\u043b\u0430\u0442\u0443", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u043d\u0438\u043a\u0443", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.users_page), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.log_browser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI Black'; font-size:8pt;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAYBOT", None))
    # retranslateUi

