import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit
)


class Components:

    @staticmethod
    def button(parent, **kwargs):
        output = QPushButton(parent)
        output.setText(kwargs["text"])
        output.setEnabled(kwargs["enabled"])
        output.setIcon(QIcon("icons/", kwargs["iconcls"]))
        return output

    @staticmethod
    def textfield(parent, **kwargs):
        output = QLineEdit(parent)
        output.textChanged.connect(lambda: kwargs["taskid"])



    def poep(self):
        sender = self.sender()


""""
TODO
panel
container
textview
textfield
icon
buttonbar

button
:actionid, enabled, iconcls, taskid, text, value
"""
