import sys
import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QGridLayout,
    QBoxLayout
)


class Components:

    @staticmethod
    def buttonbar():
        return QBoxLayout(0)

    @staticmethod
    def button(enabled=True, iconCls=None, text="", parent=None):
        output = QPushButton(parent)
        output.setText(text)
        output.setEnabled(enabled)
        output.setIcon(QIcon("icons/" + iconCls))
        return output

    @staticmethod
    def container(parent=None, direction=0, marginBottom=0, marginTop=0,
                  marginLeft=0, marginRight=0):
        output = QBoxLayout(direction)
        output.setParent(parent)
        output.setContentsMargins(marginBottom, marginTop, marginLeft,
                                  marginRight)
        return output

    @staticmethod
    def icon(iconCls, parent=None):
        output = QLabel(
            "<html><img src='icons/" + Components.create_attributes_string(
                iconCls) + ".png'></html>")
        output.setParent(parent)
        output.margin()
        return output

    @staticmethod
    def textfield(parent=None, hint="", value=None):
        output = QLineEdit(parent)
        output.setText(value)
        # output.textChanged.connect() : TODO
        output.toolTip(hint)
        return output

    @staticmethod
    def create_attributes_string(attributes_dict):
        temp = ""
        for attribute_key, attribute_value in attributes_dict.items():
            temp += " {name}=\"{value}\"".format(
                name=attribute_key,
                value=attribute_value
            )
        return temp


""""
TODO
panel
container
textview
textfield

icon
:hint, hint-type, iconCls, marginleft, tooltip
buttonbar

button
:actionid, enabled, iconCls, taskid, text, value
"""
