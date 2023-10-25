from converter import *
converter = UIConverter()
converter.convert_all_files()

from database_module import GetAllUsers, GetOneUser, GetAllOrders, GetOneOrder
from Ui.useritem_ui import Ui_UserItemForm
import database_module
from PySide6.QtGui import QTextCursor
from dis_bot import BotThread
from notifications import NotificationManager
import Ui.images_rc
from Ui.item_ui import Ui_Form
from Ui.mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QPoint, QSettings, Signal
from PySide6.QtGui import QIcon, QAction, QFontDatabase, QGuiApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
import time
import sys
from PySide6.QtCore import QThread, Signal



class UserItemWidget(QWidget, Ui_UserItemForm):
    cancel_order_signal = Signal(int)

    def __init__(self, item, userID, parent=None):
        super(UserItemWidget, self).__init__(parent)
        self.item = item
        self.setupUi(self)
        self.associated_item = self.item
        self.userID = userID

    def set_user_data(self, nickname, card_number, bank_name, balance):
        self.nick_label.setText(str(nickname))
        self.card_number_label.setText(str(card_number))
        self.bank_name_label.setText(str(bank_name))
        self.balance_label.setText(f'{str(balance)} р.')


class StreamToTextBrowser:
    def __init__(self, text_browser):
        self.log_browser = text_browser

    def write(self, text):
        cleaned_text = text.strip()
        if cleaned_text:
            self.log_browser.append(cleaned_text)
            cursor = self.log_browser.textCursor()
            cursor.movePosition(QTextCursor.End)
            self.log_browser.setTextCursor(cursor)

    def flush(self):
        pass


class OrderItemWidget(QWidget, Ui_Form):
    cancel_order_signal = Signal(int)

    def __init__(self, item, wid_id, parent=None):
        super(OrderItemWidget, self).__init__(parent)
        self.item = item
        self.setupUi(self)
        self.associated_item = self.item
        self.widget_id = wid_id
        self.pushButton.clicked.connect(self.remove_order_click)

    def set_order_data(self, nickname, amount, disc):
        self.label.setText(nickname)
        self.label_2.setText(f'{amount} р.')
        self.label_3.setText(disc)

    def remove_order(self):
        self.label.setText(f'<font color=#aa5500>{self.label.text()}</font>')
        self.label_2.setText(
            f'<font color=#aa5500>{self.label_2.text()}</font>')
        self.label_3.setText(
            f'<font color=#aa5500>{self.label_3.text()}</font>')
        self.pushButton.setText('Отменен')
        self.pushButton.setEnabled(False)

    def remove_order_click(self):
        self.label.setText(f'<font color=#aa5500>{self.label.text()}</font>')
        self.label_2.setText(
            f'<font color=#aa5500>{self.label_2.text()}</font>')
        self.label_3.setText(
            f'<font color=#aa5500>{self.label_3.text()}</font>')
        self.pushButton.setText('Отменен')
        self.pushButton.setEnabled(False)
        self.cancel_order_signal.emit(self.widget_id)
        session = database_module.Session()
        order_cancel = session.query(database_module.Order).filter_by(
            id=self.widget_id).first()
        change_balance = session.query(database_module.User).filter_by(
            id=order_cancel.user_id).first()
        if change_balance and int(change_balance.balance) >= int(order_cancel.amount):
            change_balance.balance = int(
                change_balance.balance) - int(order_cancel.amount)
        if order_cancel:
            order_cancel.deleted = True
            session.commit()
            session.close()
        # self.bot_thread.edit_message(1134556255424348220, 1165792792333791245)


class MainWindow(QMainWindow, Ui_MainWindow):
    log_received = Signal(str)  # Signal for logging
    message_received = Signal(str, str)  # Signal for author and message

    def __init__(self):
        super(MainWindow, self).__init__()
        self.settings = QSettings("config.ini", QSettings.IniFormat)
        self.load_window_settings()
        self.appvisible = True
        self.offset = None
        # Set the application icon
        self.setWindowIcon(QIcon(":/img/icon20.png"))

        # Remove system border and title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Make the window background transparent
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        self.setupUi(self)

        # sys.stdout = StreamToTextBrowser(self.log_browser)
        # sys.stderr = StreamToTextBrowser(self.log_browser)

        self.add_log('Приложение запущено', 'INFO')
        self.add_log(
            'Твой ключ: RT_jSidC9viIgmuLSFbud4wXk0h7xUBNqyNvAdszQSsMZPyvE (31 дней)', 'INFO')
        self.tabWidget.setCurrentIndex(0)
        self.index_page_btn.setEnabled(False)

        self.notify = NotificationManager(self)
        self.discord_starter()

        self.profile_window = None

        # Set the window title
        self.setWindowTitle("Payment")
        # Setup system tray icon
        self.tray_icon = QSystemTrayIcon(self)
        # Replace with the path to your icon
        self.tray_icon.setIcon(QIcon(":/img/icon20.png"))
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        # Set tooltip for the tray icon
        self.tray_icon.setToolTip("RT APP")

        tray_menu = QMenu()
        restore_action = QAction("Restore", self)
        quit_action = QAction("Exit", self)

        restore_action.triggered.connect(self.show)
        quit_action.triggered.connect(app.quit)

        tray_menu.addAction(restore_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Connect signals for the close and minimize buttons
        self.close_btn.clicked.connect(self.close_window)
        self.minimize_btn.clicked.connect(
            self.minimize_to_tray)  # Modify for minimize to tray

        screens = QGuiApplication.screens()
        for index, screen in enumerate(screens):
            self.comboBox_2.insertItem(index, screen.name())

        self.notify_position = self.settings.value("notify_pos")
        self.notify_mon = self.settings.value("notify_mon")

        if not self.notify_position:
            self.settings.setValue("notify_pos", 'bottom-right')
            self.notify_position = self.settings.value("notify_pos")
        if not self.notify_mon:
            self.settings.setValue("notify_mon", 0)
            self.notify_mon = self.settings.value("notify_mon")

        self.comboBox_2.setCurrentIndex(int(self.notify_mon))
        self.comboBox.setCurrentText(self.notify_position)

        self.index_page_btn.clicked.connect(lambda: self.setPage('main_page'))
        self.settings_page_btn.clicked.connect(
            lambda: self.setPage('settings_page'))
        self.stat_page_btn.clicked.connect(lambda: self.setPage('stat_page'))
        self.payment_page_btn.clicked.connect(
            lambda: self.setPage('payment_page'))
        self.users_page_btn.clicked.connect(lambda: self.setPage('users_page'))
        self.pushButton_3.clicked.connect(self.seApiToken)
        self.pushButton_5.clicked.connect(self.discord_starter)
        self.comboBox.currentIndexChanged.connect(self.notify_pos)
        self.comboBox_2.currentIndexChanged.connect(self.notify_monitor)
        self.pushButton.clicked.connect(self.testnotify)
        self.textEdit.setEnabled(False)

        self.lineEdit_3.textChanged.connect(self.filter_items)
        self.listWidget.setSelectionMode(QListWidget.NoSelection)
        self.UsersListWidget.setSelectionMode(QListWidget.NoSelection)
        self.pushButton_4.clicked.connect(self.addWidg)
        self.listWidget.scrollToBottom()
        self.widget.hide()

        


        usersList = GetAllUsers()

        for user in usersList:
            item = QListWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            self.UsersListWidget.addItem(item)
            widget = UserItemWidget(item, user.id, self.UsersListWidget)
            widget.set_user_data(user.username, user.card_number, user.bank_name, user.balance)
            self.UsersListWidget.setItemWidget(item, widget)


        session = database_module.Session()
        orders = session.query(database_module.Order).all()

        for order in orders:
            nickname = order.user.username
            amount = order.amount
            discription = order.desc
            item = QListWidgetItem()
            item.setFlags(Qt.NoItemFlags)
            self.listWidget.addItem(item)
            widget = OrderItemWidget(item, order.id, self.listWidget)
            widget.cancel_order_signal.connect(self.canc_order)
            widget.set_order_data(nickname, amount, discription)
            if order.deleted:
                widget.remove_order()
            self.listWidget.setItemWidget(item, widget)

    def canc_order(self, id):
        orders_c = GetOneOrder(id)
        self.bot_thread.edit_message(orders_c.chat_id, orders_c.msg_id)


    def filter_items(self, text):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            widget = self.listWidget.itemWidget(item)
            if widget:
                item.setHidden(text.lower() not in widget.label.text().lower())

    def addWidg(self):
        nickname = self.lineEdit_4.text()
        amount = self.lineEdit_6.text()
        discription = self.lineEdit_5.text()
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.listWidget.addItem(item)
        widget = OrderItemWidget(item, self.listWidget)
        widget.cancel_order_signal.connect(self.canc_order)
        widget.set_order_data(nickname, amount, discription)
        self.listWidget.setItemWidget(item, widget)

        self.listWidget.scrollToBottom()

    def find_widget_in_list(self, qlistwidget, widget_id):
        for index in range(qlistwidget.count()):
            item = qlistwidget.item(index)
            widget = qlistwidget.itemWidget(item)
            if widget and hasattr(widget, 'widget_id') and widget.widget_id == widget_id:
                return widget
        return None

    def disCancelPayment(self, wid_id):
        widget = self.find_widget_in_list(self.listWidget, wid_id)
        if widget:
            widget.label.setText(
                f'<font color=#aa5500>{widget.label.text()}</font>')
            widget.label_2.setText(
                f'<font color=#aa5500>{widget.label_2.text()}</font>')
            widget.label_3.setText(
                f'<font color=#aa5500>{widget.label_3.text()}</font>')
            widget.pushButton.setText('Отменен')
            widget.pushButton.setEnabled(False)

    def disPayment(self, nickname, ord_id, summ, disc):
        self.notify_position = self.settings.value("notify_pos")
        self.notify_mon = self.settings.value("notify_mon")
        self.notify.add(f'<b>   {nickname}</b> <br> Cоздает заявку на выплату {summ} руб. <br>Примечание: {disc}',
                        30001, self.notify_position, int(self.notify_mon))
        item = QListWidgetItem()
        item.setFlags(Qt.NoItemFlags)
        self.listWidget.addItem(item)
        widget = OrderItemWidget(item, ord_id, self.listWidget)
        widget.cancel_order_signal.connect(self.canc_order)
        widget.set_order_data(nickname, summ, disc)
        self.listWidget.setItemWidget(item, widget)

        self.listWidget.scrollToBottom()

    def testnotify(self):
        self.notify.add(f'Test notify', 1000, self.comboBox.currentText(
        ), self.comboBox_2.currentIndex())

    def notify_monitor(self):
        self.settings.setValue("notify_mon", self.comboBox_2.currentIndex())
        self.add_log(
            f'Монитор для оповещений изменен - {self.comboBox_2.currentText()}', 'INFO')

    def notify_pos(self):
        self.settings.setValue("notify_pos", self.comboBox.currentText())
        self.add_log(
            f'Расположение оповещений изменено {self.comboBox.currentText()}', 'INFO')

    def seApiToken(self):
        if self.lineEdit_2:
            self.settings.setValue("api_token", self.lineEdit_2.text())
            self.add_log(
                'API Token Изменен, настройки применятся при перзагрузке приложения!', 'INFO')

    def discord_starter(self):
        self.token = self.settings.value("api_token")
        if self.token == None or self.token == '' or self.token == 'None':
            self.add_log('Токен не добавлен!', 'WARN')
        else:
            self.lineEdit_2.setText(self.token)
            self.add_log('Подключаю дискорд...', 'INFO')
            self.bot_thread = BotThread(self.token)
            self.bot_thread.log_signal.connect(self.log_received)
            self.bot_thread.message_signal.connect(self.message_received)
            self.bot_thread.start()
            self.log_received.connect(self.disLog)
            self.message_received.connect(self.disMsg)
            self.pushButton_5.setEnabled(False)
            self.bot_thread.payment_signal.connect(self.disPayment)
            self.bot_thread.cancel_order_signal.connect(self.disCancelPayment)

    def disLog(self, text):
        self.add_log(f'<font color = green>{text}</green>', 'INFO')

    def disMsg(self, login, msg):
        self.notify_position = self.settings.value("notify_pos")
        self.notify_mon = self.settings.value("notify_mon")
        self.n_pos = "bottom-right"
        self.n_mon = 0
        if self.notify_position:
            self.n_pos = self.notify_position
        if self.notify_mon:
            self.n_mon = int(self.notify_mon)
        self.add_log(f'{login} - {msg}', 'INFO')
        self.notify.add(f'{login} - {msg}', 50000, self.n_pos, self.n_mon)

    def setPage(self, page):
        self.enabelAllBtn()
        if page == 'main_page':
            self.tabWidget.setCurrentIndex(0)
            self.index_page_btn.setEnabled(False)
        if page == 'settings_page':
            self.tabWidget.setCurrentIndex(1)
            self.settings_page_btn.setEnabled(False)
        if page == 'stat_page':
            self.tabWidget.setCurrentIndex(2)
            self.stat_page_btn.setEnabled(False)
        if page == 'payment_page':
            self.tabWidget.setCurrentIndex(3)
            self.payment_page_btn.setEnabled(False)
        if page == 'users_page':
            self.tabWidget.setCurrentIndex(4)
            self.users_page_btn.setEnabled(False)

    def enabelAllBtn(self):
        self.index_page_btn.setEnabled(True)
        self.settings_page_btn.setEnabled(True)
        self.stat_page_btn.setEnabled(True)
        self.payment_page_btn.setEnabled(True)
        self.users_page_btn.setEnabled(True)

    def add_log(self, text, status):
        time_string = time.strftime("%H:%M:%S", time.localtime())
        if status == 'INFO':
            status = '<font color = #55aaff>[INFO]</font>'
        if status == 'WARN':
            status = '<font color = #d54700>[WARN]</font>'
        self.log_browser.append(
            f"<font color = #bcd48d>{time_string}</font> - {status} - <font color = white>{text}</font>")

    def load_api_settings(self):
        print(self.settings.value("api_token", 'sdsd'))

    def load_window_settings(self):
        # Загрузите положение и размер окна из настроек
        self.move(self.settings.value("window_position", QPoint(100, 100)))

    def save_window_settings(self):
        # Сохраните текущее положение и размер окна в настройках
        self.settings.setValue("window_position", self.pos())

    def closeEvent(self, event):
        self.save_window_settings()
        super().closeEvent(event)

    def close_window(self):
        """Slot to handle the close button click."""
        self.close()

    def minimize_to_tray(self):   # Modify for minimize to tray
        """Slot to handle the minimize button click."""
        self.appvisible = False
        self.hide()

    def on_tray_icon_activated(self, reason):
        """Slot to handle tray icon activation (e.g. double click)"""
        if reason == QSystemTrayIcon.DoubleClick:
            if self.appvisible:
                self.hide()
                self.appvisible = False
            else:
                self.show()
                self.appvisible = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(), event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            if self.offset.y() < self.headwidget.rect().bottomLeft().y() + 5:
                self.move(self.pos() + QPoint(event.scenePosition().x(),
                          event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(":/font/SHOWG.TTF")
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
