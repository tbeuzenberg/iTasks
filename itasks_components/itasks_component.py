"""Itasks_component for use in a Node"""
# pylint: disable-msg=too-few-public-methods
from PyQt5.QtWidgets import QLayout, QWidget, QPushButton, QLineEdit, QLabel


class ItasksComponent:
    """
    Component which is used to cluster iTask-specific attributes.
    Used as "value" attribute in a Node.
    """

    def __init__(self, qwidget: QWidget, qlayout: QLayout, action_id=None,
                 task_id=None, main=False, editor_id=None):
        """
        :param qwidget: widget to add to component
        :param action_id: action_id assigned to this component by iTasks
        :param task_id: task_id assigned to this component by iTasks
        :param qlayout: layout to sort this component with
        """
        self.action_id = action_id
        self.task_id = task_id
        self.editor_id = editor_id
        self.qwidget = qwidget
        self.qlayout = qlayout
        self.main = main
        if main:
            self.qwidget.setLayout(self.qlayout)
        else:
            self.qlayout.addWidget(self.qwidget)

    def reset(self, children):
        """" Hides the qwidget and sets action_id and task_id to None """
        self.action_id = None
        self.task_id = None

        if len(children) > 0:
            self.qwidget.hide()

    def update(self, arguments):
        """
        Update ItasksComponent
        :param arguments: array of name, value pairs to update
        example: [ { "name": "hint", "value": "valid text" } ]
        """
        qwidget = self.qwidget
        self.qlayout.removeWidget(self.qwidget)

        dictionary = {}
        for arg in arguments:
            dictionary.update({arg["name"]: arg["value"]})

        if isinstance(qwidget, QPushButton):
            self.__update_button(qwidget, dictionary)

        if isinstance(qwidget, QLineEdit):
            self.__update_textfield(qwidget, dictionary)

        if isinstance(qwidget, QLabel):
            self.__update_icon(qwidget, dictionary)

        self.qlayout.addWidget(qwidget)
        self.qwidget = qwidget

    def __update_icon(self, qwidget, dictionary):  # pragma: no cover
        """"
        Ignored in coverage as it's tested through update method
        Update qwidget's icon
        :param qwidget: QWidget to update icon of
        :param dictionary: dictionary from update function
        """
        if 'iconCls' in dictionary:
            icon = dictionary.pop('iconCls')
            qwidget.setText(
                "<html><img src='icons/" + icon + ".png'></html>"
            )

    def __update_button(self, qwidget, dictionary):  # pragma: no cover
        """"
        Ignored in coverage as it's tested through update method
        Update QPushButton11
        :param qwidget: QPushButton to update
        :param dictionary: dictionary from update function
        """
        if 'text' in dictionary:
            text = dictionary.pop('text')
            qwidget.setText(text)

        if 'enabled' in dictionary:
            enabled = dictionary.pop('enabled')
            qwidget.setEnabled(enabled)

        if 'iconCls' in dictionary:
            icon = dictionary.pop('iconCls')
            qwidget.setIcon("icons/" + icon + ".png")

    def __update_textfield(self, qwidget, dictionary):  # pragma: no cover
        """"
        Ignored in coverage as it's tested through update method
        Update QLineEdit
        :param qwidget: QLineEdit to update
        :param dictionary: dictionary from update function
        """
        if 'value' in dictionary:
            value = dictionary.pop('value')
            qwidget.setText(value)

        if 'hint' in dictionary:
            hint = dictionary.pop('hint')
            qwidget.setToolTip(hint)
