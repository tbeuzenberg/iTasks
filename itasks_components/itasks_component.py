"""Itasks_component for use in a Node"""
# pylint: disable-msg=too-few-public-methods
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLayout, QWidget


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
        self.action_id = None
        self.task_id = None

        for child in children:
            self.qlayout.removeWidget(child.value.qwidget)
            child.value.qwidget.deleteLater()

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

        self.__update_icon(qwidget, dictionary)
        self.__update_value(qwidget, dictionary)
        self.__update_hint(qwidget, dictionary)

        for arg in dictionary:
            qwidget.setProperty(arg, dictionary.get(arg))

        self.qlayout.addWidget(qwidget)
        self.qwidget = qwidget

    def __update_icon(self, qwidget, dictionary):
        """"
        Update qwidget's icon
        :param qwidget: QWidget to update icon of
        :param dictionary: dictionary from update function
        """
        if 'iconCls' in dictionary:
            icon = dictionary.pop('iconCls')
            qwidget.setIcon(QIcon('icons/' + icon))

    def __update_value(self, qwidget, dictionary):
        """"
        Update textfield's text value
        :param qwidget: QWidget to update value of
        :param dictionary: dictionary from update function
        """
        if 'value' in dictionary:
            value = dictionary.pop('value')
            qwidget.setText(value)

    def __update_hint(self, qwidget, dictionary):
        """"
        Update qwidgets's hint
        :param qwidget: QWidget to update hint of
        :param dictionary: dictionary from update function
        """
        if 'hint' in dictionary:
            hint = dictionary.pop('hint')
            qwidget.setTooltip(hint)

        if 'hint-type' in dictionary:
            hint_type = dictionary.pop('hint-type')
            if hint_type == "valid":
                qwidget.setIcon(QIcon('icons/accept.png'))
            else:
                qwidget.setIcon(QIcon('icons/icon-info.png'))
