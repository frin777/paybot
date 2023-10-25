import sys
import threading
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QHBoxLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QCursor
from PySide6.QtGui import QPixmap
import Ui.images_rc

class NotificationWidget(QWidget):
    def __init__(self, message, manager, position="bottom-right", timeout=5000, screen_index=0):
        super().__init__(None, Qt.WindowDoesNotAcceptFocus)
        self.message = message
        self.timeout = timeout
        self.position = position
        self.manager = manager
        self.screen_index = screen_index  # добавлен индекс экрана
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setAutoFillBackground(True)
        self.setStyleSheet("""
            background-color: rgba(36, 36, 37, 222);
            border: 1px solid rgb(45, 45, 45);
            color: rgb(185, 185, 185);
            border-radius: 2px;
            padding: 10px;
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))

        layout = QVBoxLayout()
        hlayout = QHBoxLayout()  # Горизонтальное размещение для изображения и текста
        hlayout.setContentsMargins(0, 0, 0, 0)
        hlayout.setSpacing(0)  # Это установит расстояние между элементами в компоновке


        # Добавляем изображение
        pixmap = QPixmap(":/img/msg3.png")  # Замените "image.png" на путь к вашему изображению
        self.image_label = QLabel(self)
        self.image_label.setStyleSheet("""
            background-color: rgba(36, 36, 37, 222);
            border: 1px solid rgb(45, 45, 45);
            color: rgb(185, 185, 185);
            border-radius: 0px;
            padding: 10px;
        """)
        self.image_label.setPixmap(pixmap.scaled(32, 32, Qt.KeepAspectRatio))  # Масштабирование изображения
        hlayout.addWidget(self.image_label)

        self.label = QLabel(self.message)
        self.label.setFixedWidth(250)  # Например, установите ширину в 280 пикселей
        self.label.setWordWrap(True)   # Включите автоматический перенос слов
        self.label.setStyleSheet("""
            background-color: rgba(36, 36, 37, 222);
            border: 1px solid rgb(45, 45, 45);
            color: rgb(185, 185, 185);
            border-radius: 0px;
            padding: 1px;
        """)
        hlayout.addWidget(self.label)
        layout.addLayout(hlayout)  # Добавляем горизонтальное размещение в основной компоновке
        
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.setFixedSize(300, 60)  # Увеличиваем размер чтобы уместить и изображение, и текст

        if self.timeout:
            QTimer.singleShot(self.timeout, self.close_notification)

    def close_notification(self):
        self.manager.notification_closed(self)
        self.close()

    def mousePressEvent(self, event):
        self.close_notification()

class NotificationManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.notifications_queue_bottom = []
        self.notifications_queue_top = []
        self.notifications_queue_left_top = []
        self.notifications_queue_left_bottom = []
        self.active_notifications_bottom = []
        self.active_notifications_top = []
        self.active_notifications_left_top = []
        self.active_notifications_left_bottom = []
        self.notification_counter = 0
        self.lock = threading.Lock()

    def add(self, message, timeout=5000, position="bottom-right", screen_index=0):
        with self.lock:
            self.notification_counter += 1
            notification_message = f"{message}"
            # notification_message = f"{self.notification_counter}: {message}" # с нумерацией для отладки
        
        if position == "bottom-right":
            self.handle_notification(self.active_notifications_bottom, self.notifications_queue_bottom, notification_message, position, timeout, screen_index)
        elif position == "top-right":
            self.handle_notification(self.active_notifications_top, self.notifications_queue_top, notification_message, position, timeout, screen_index)
        elif position == "left-top":
            self.handle_notification(self.active_notifications_left_top, self.notifications_queue_left_top, notification_message, position, timeout, screen_index)
        elif position == "left-bottom":
            self.handle_notification(self.active_notifications_left_bottom, self.notifications_queue_left_bottom, notification_message, position, timeout, screen_index)

    def handle_notification(self, active_notifications, notifications_queue, message, position, timeout, screen_index):
        if len(active_notifications) < 5:
            notification = NotificationWidget(message, self, position=position, timeout=timeout, screen_index=screen_index)
            self.position_notification(notification, len(active_notifications), position, screen_index)
            notification.show()
            active_notifications.append(notification)
        else:
            notifications_queue.append((message, screen_index))

    def position_notification(self, notification, idx=0, position="bottom-right", screen_index=0):
        screen_geometry = QApplication.screens()[screen_index].availableGeometry()

        if position == "bottom-right":
            x = screen_geometry.x() + screen_geometry.width() - notification.width() - 10
            y = screen_geometry.y() + screen_geometry.height() - (notification.height() + 10) * (idx + 1)
        elif position == "top-right":
            x = screen_geometry.x() + screen_geometry.width() - notification.width() - 10
            y = screen_geometry.y() + 10 + (notification.height() + 10) * idx
        elif position == "left-top":
            x = screen_geometry.x() + 10
            y = screen_geometry.y() + 10 + (notification.height() + 10) * idx
        elif position == "left-bottom":
            x = screen_geometry.x() + 10
            y = screen_geometry.y() + screen_geometry.height() - (notification.height() + 10) * (idx + 1)

        notification.move(x, y)

    def notification_closed(self, closed_notification):
        if closed_notification in self.active_notifications_bottom:
            self.update_notifications("bottom-right", closed_notification, self.active_notifications_bottom, self.notifications_queue_bottom)
        elif closed_notification in self.active_notifications_top:
            self.update_notifications("top-right", closed_notification, self.active_notifications_top, self.notifications_queue_top)
        elif closed_notification in self.active_notifications_left_top:
            self.update_notifications("left-top", closed_notification, self.active_notifications_left_top, self.notifications_queue_left_top)
        elif closed_notification in self.active_notifications_left_bottom:
            self.update_notifications("left-bottom", closed_notification, self.active_notifications_left_bottom, self.notifications_queue_left_bottom)

    def update_notifications(self, position, closed_notification, active_notifications, notifications_queue):
        active_notifications.remove(closed_notification)
        for idx, notification in enumerate(active_notifications):
            self.position_notification(notification, idx, position, notification.screen_index)  # используйте screen_index из notification
        if notifications_queue and len(active_notifications) < 5:
            message, screen_index = notifications_queue.pop(0)
            notification = NotificationWidget(message, self, position=position, screen_index=screen_index)
            self.position_notification(notification, len(active_notifications), position, screen_index)
            notification.show()
            active_notifications.append(notification)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.notify = NotificationManager(self)

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.btn_bottom = QPushButton('Отправить оповещение (низ)', self)
        self.btn_bottom.clicked.connect(lambda: self.notify.add("Это ваше оповещение в правом нижнем углу!", 50000, "bottom-right", 0))
        layout.addWidget(self.btn_bottom)


        self.btn_top = QPushButton('Отправить оповещение (верх)', self)
        self.btn_top.clicked.connect(lambda: self.notify.add("Это ваше оповещение в правом верхнем углу!", 50000, "top-right", 0))
        layout.addWidget(self.btn_top)

        self.btn_left_top = QPushButton('Отправить оповещение (лево верх)', self)
        self.btn_left_top.clicked.connect(lambda: self.notify.add("Это ваше оповещение\n в левом \nверхнем углу!", 50000, "left-top", 0))
        layout.addWidget(self.btn_left_top)

        self.btn_left_bottom = QPushButton('Отправить оповещение (лево низ)', self)
        self.btn_left_bottom.clicked.connect(lambda: self.notify.add("Это ваше оповещение в левом нижнем углу!", 50000, "left-bottom", 0))
        layout.addWidget(self.btn_left_bottom)


        self.btn_show_screens = QPushButton('Показать количество экранов', self)
        self.btn_show_screens.clicked.connect(self.show_screens_count)
        layout.addWidget(self.btn_show_screens)

        self.setCentralWidget(central_widget)
        self.resize(300, 200)

    def show_screens_count(self):
        count = len(QApplication.screens())
        self.notify.add(f"У вас {count} мониторов", 5000, "bottom-right", 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
