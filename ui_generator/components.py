import sys
import time


from PyQt5.QtCore import Qt

from PyQt5.QtGui import (
    QIcon,
    QPalette
)
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QGridLayout,
    QWidget,
    QHBoxLayout,
    QBoxLayout
)


class Components:

    @staticmethod
    def buttonbar():
        return QBoxLayout(0)

    @staticmethod
    def button(enabled=True, iconCls=None, text="",
               parent=None, height=100, width=200, **kwargs):
        output = QPushButton(parent)
        output.setGeometry(0, 0, width, height)
        output.setText(text)
        output.setEnabled(enabled)
        output.setIcon(QIcon("icons/" + iconCls))
        return output

    @staticmethod
    def container(parent=None, direction=0, marginBottom=0, marginTop=0,
                  marginLeft=0, marginRight=0, **kwargs):
        output = QBoxLayout(direction)
        output.setParent(parent)
        output.setContentsMargins(marginBottom, marginTop, marginLeft,
                                  marginRight)
        return output

    @staticmethod
    def icon(iconCls, parent=None, **kwargs):
        output = QLabel(
            "<html><img src='icons/" + iconCls + ".png'></html>")
        output.setParent(parent)
        output.margin()
        return output

    @staticmethod
    def textfield(hint="", value=None, parent=None, **kwargs):
        output = QLineEdit()
        output.setParent(parent)
        output.setText(value)
        # output.textChanged.connect() : TODO
        return output

    @staticmethod
    def label(parent=None, **kwargs):
        output = QLabel()
        output.setParent(parent)
        output.setText(kwargs["value"])
        return output

    @staticmethod
    def create_html_attributes(attributes_dict):
        temp = ""
        for attribute_key, attribute_value in attributes_dict.items():
            temp += " {name}=\"{value}\"".format(
                name=attribute_key,
                value=attribute_value
            )
        return temp

    @staticmethod
    def buttonbar(parent=None, **kwargs):
        output = QWidget(parent=parent)
        output.setLayout(QHBoxLayout())

        return output

    @staticmethod
    def unknown_component(parent=None, **kwargs):
        raise NotImplementedError

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
