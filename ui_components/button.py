import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QPushButton,
)


class Button:
    def __new__(cls, parent, **kwargs):
        output = QPushButton(parent)
        output.setText(kwargs["text"])
        output.setEnabled(kwargs["enabled"])
        output.setIcon(QIcon("icons/", kwargs["iconcls"]))
        return output



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
