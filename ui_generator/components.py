# pylint: disable-msg=unused-argument

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
    def component(qwidget, marginBottom=0, marginTop=0, marginLeft=0, marginRight=0, **kwargs):
        qwidget.setContentsMargins(marginBottom, marginTop, marginLeft, marginRight)
        return qwidget

    @staticmethod
    def buttonbar(qwidget):
        return QBoxLayout(0)


    @staticmethod
    def button(enabled=True, iconCls=None, text="", parent=None, **kwargs):
        output = QPushButton(parent)
        output = Components.component(output, **kwargs)

        output.setText(text)
        output.setEnabled(enabled)
        output.setIcon(QIcon("icons/" + iconCls))
        return output

    @staticmethod
    def container(parent=None, **kwargs):
        output = QWidget(parent)
        output = Components.component(output, **kwargs)
        return output

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
