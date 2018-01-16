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
                 task_id=None, main=False):
        """
        :param qwidget: widget to add to component
        :param action_id: action_id assigned to this component by iTasks
        :param task_id: task_id assigned to this component by iTasks
        :param qlayout: layout to sort this component with
        """
        self.action_id = action_id
        self.task_id = task_id
        self.qwidget = qwidget
        self.qlayout = qlayout
        if main:
            self.qwidget.setLayout(self.qlayout)
        else:
            self.qlayout.addWidget(self.qwidget)

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

        self.__update_geometry(qwidget, dictionary)
        self.__update_icon(qwidget, dictionary)

        for arg in dictionary:
            qwidget.setProperty(arg, dictionary.get(arg))

        self.qlayout.addWidget(qwidget)
        self.qwidget = qwidget

    def __update_geometry(self, qwidget, dictionary):
        """"
        Update qwidget's geometry
        :param qwidget: QWidget to update geometry of
        :param dictionary: dictionary from update function
        """
        if 'x' in dictionary or \
                'y' in dictionary or \
                'width' in dictionary or \
                'height' in dictionary:
            x = dictionary.pop('x') if 'x' in dictionary else qwidget.x()
            y = dictionary.pop('y') if 'y' in dictionary else qwidget.y()
            width = dictionary.pop('width') if 'width' in dictionary \
                else qwidget.width()
            height = dictionary.pop('height') if 'height' in dictionary \
                else qwidget.height()

            qwidget.setGeometry(x, y, width, height)

    def __update_icon(self, qwidget, dictionary):
        """"
        Update qwidget's geometry
        :param qwidget: QWidget to update icon of
        :param dictionary: dictionary from update function
        """
        if 'icon' in dictionary:
            icon = dictionary.pop('icon')
            qwidget.setIcon(QIcon(icon))
