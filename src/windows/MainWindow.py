"""
...
"""

import datetime

import PyQt5.QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QMainWindow
from pythonosc import udp_client

from forms.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """
    ...
    """

    def __init__(self):
        """
        ...
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.osc_client = udp_client.SimpleUDPClient("127.0.0.1", 9000)

        self.ui.send_button.clicked.connect(self.handle_send)

        self.ui.message_field.installEventFilter(self)

        self.ui.language_selector.currentIndexChanged.connect(
            self.handle_language_change
        )

    def handle_language_change(self) -> None:
        print("selection changed")

    def handle_send(self) -> None:
        """
        ...
        """
        message = self.ui.message_field.toPlainText()
        if not message:
            return

        self.osc_client.send_message("/chatbox/input", [message, True, False])

        date = datetime.datetime.now().isoformat(timespec="seconds")
        self.ui.log_field.appendHtml(f'<font color="gray">[{date}]:</font> {message}')
        self.ui.message_field.clear()
        self.ui.message_field.setFocus()

    def eventFilter(self, obj, event):
        """
        ...
        """
        if (
            event.type() == PyQt5.QtCore.QEvent.KeyPress
            and obj is self.ui.message_field
        ):
            key_pressed = event.key()

            if key_pressed == PyQt5.QtCore.Qt.Key_Return:
                self.handle_send()
                return True

        return False
