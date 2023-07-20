"""
...
"""

import datetime

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

        self.udp_client = udp_client.SimpleUDPClient("localhost", 9000)

        self.ui.send_button.clicked.connect(self.handle_send)
        self.ui.message_field.textChanged.connect(self.handle_text_changed)

    def handle_text_changed(self):
        """
        ...
        """
        pass

    def handle_send(self):
        """
        ...
        """
        message = self.ui.message_field.toPlainText()
        if not message:
            return

        self.udp_client.send_message("/chatbox/input", [message, True, False])

        date = datetime.datetime.now().isoformat(timespec="seconds")
        self.ui.log_field.appendHtml(f'<font color="gray">[{date}]:</font> {message}')
        self.ui.message_field.clear()
        self.ui.message_field.setFocus()
