"""File for Components class"""
# pylint: disable-msg=unused-argument
# pylint: disable-msg=invalid-name
from PyQt5.QtGui import (
    QIcon,
)
from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QGridLayout,
    QWidget,
    QBoxLayout,
    QLayout)

from itasks_components import ItasksComponent


class Components:
    """
    Components class. Public methods in this class can be called
    to create an ItasksComponent based on specifications
    """
    @staticmethod
    def __set_margins_and_geometry(qwidget, marginBottom=0, marginTop=0,
                                   marginLeft=0, marginRight=0, **kwargs):
        """
        This method sets the margins and geometry for the QWidget passed into it.
        :param qwidget: Qwidget to set the margins, padding and geometry for.
        :param marginBottom: Margin this qwidget has to have between elements below it and itself
        :param marginTop: Margin this qwidget has to have between elements above it and itself
        :param marginLeft: Margin this qwidget has to have between elements to the left of it
        and itself
        :param marginRight: Margin this qwidget has to have between elements to the right of it
        and itself
        :param **kwargs: Safety measure for when Itasks passes too many arguments
        :return: the Qwidget with corrected margins and geometry
        """
        qwidget.setContentsMargins(marginBottom, marginTop, marginLeft, marginRight)
        # set geometry TODO
        return qwidget

    @staticmethod
    def __nest_layout(parent: ItasksComponent, layout: QLayout, index: int = -1):
        """
        Nests the given layout in the given parent at the location of the given index.
        :param parent: parent to nest the layout into
        :param layout: layout you want to nest
        :param index: index you want the layout to be nested at
        :rtype void
        """
        if parent.qlayout is QBoxLayout:
            parent.qlayout.insertLayout(Qlayout=layout, index=index)
        else:
            parent.qlayout.addLayout(QLayout=layout, row=index, column=0)

    @staticmethod
    def buttonbar(index: int, parent: ItasksComponent, **kwargs):
        """
        Creates an ItasksComponent containing a buttonbar and a layout
        and a layout in which the buttonbar is nested
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QWidget(parent.qwidget)
        widget = Components.__set_margins_and_geometry(widget, **kwargs)

        layout = QBoxLayout(0)
        Components.__nest_layout(parent=parent, layout=layout, index=index)

        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def button(index: int, parent: ItasksComponent, enabled=True, iconCls=None, text="", **kwargs):
        """
        Creates an ItasksComponent containing a button and a layout
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param enabled: boolean that determines if the button is enabled or not
        :param iconCls: Icon class: this determines which icon is
        picked from the /icons directory
        :param text: Text that is embedded in the button
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QPushButton(parent.qwidget)
        widget.setText(text)
        widget.setEnabled(enabled)
        widget.setIcon(QIcon("icons/" + iconCls))
        widget = Components.__set_margins_and_geometry(widget, **kwargs)
        # widget.clicked.connect() TODO

        layout = QGridLayout()
        Components.__nest_layout(parent, layout, index)

        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def container(index: int, parent: ItasksComponent, **kwargs):
        """
        Creates an ItasksComponent containing a container and a layout
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QWidget(parent.qwidget)
        widget = Components.__set_margins_and_geometry(widget, **kwargs)

        layout = QGridLayout()
        Components.__nest_layout(layout=layout, index=index, parent=parent)

        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def icon(iconCls, index: int, parent: ItasksComponent, **kwargs):
        """
        Creates an ItasksComponent containing an icon and a layout
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param iconCls: Icon Class: this determines which icon is
        picked from the /icons directory
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QLabel("<html><img src='icons/" + iconCls + ".png'></html>",
                        parent=parent.qwidget)
        widget = Components.__set_margins_and_geometry(widget, **kwargs)

        layout = QGridLayout()
        Components.__nest_layout(parent=parent, layout=layout, index=index)

        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def textfield(parent: ItasksComponent, index: int, hint="", value=None, **kwargs):
        """
        Creates an ItasksComponent containing an icon and a layout
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param hint: text for the tooltip
        :param value: text in the field
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QLineEdit(parent.qwidget)
        widget.setText(value)
        widget.setToolTip(hint)
        widget = Components.__set_margins_and_geometry(qwidget=widget, **kwargs)

        layout = QGridLayout()
        Components.__nest_layout(parent=parent, layout=layout, index=index)

        # output.textChanged.connect() : TODO
        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def label(parent: ItasksComponent, index: int, text, **kwargs):
        """
        Creates an ItasksComponent containing a label and a layout
        :param index: index you want the item to be nested at
        :param parent: parent to nest the item into
        :param text: text to put in the label
        :param kwargs: remaining arguments
        :return: returns a filled ItasksComponent
        :rtype ItasksComponent
        """
        widget = QLabel(parent.qwidget)
        widget = Components.__set_margins_and_geometry(qwidget=widget, **kwargs)

        layout = QGridLayout()
        Components.__nest_layout(parent=parent, layout=layout, index=index)

        output = ItasksComponent(qwidget=widget, qlayout=layout, **kwargs)
        return output

    @staticmethod
    def unknown_component(parent=None, **kwargs):
        """
        Unknown component, not implemented yet
        :param parent:
        :param kwargs:
        :return:
        """
        pass
        # raise NotImplementedError
