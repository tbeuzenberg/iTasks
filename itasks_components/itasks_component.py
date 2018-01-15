"""Itasks_component for use in a Node"""
# pylint: disable-msg=too-few-public-methods
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLayout, QWidget


class ItasksComponent:
    """
    Component which is used to cluster iTask-specific attributes.
    Used as "value" attribute in a Node.
    """
    def __init__(self, qwidget:QWidget, qlayout:QLayout, action_id=None, task_id=None, main=False):
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

    def update(self, **kwargs):
        """
        Update ItasksComponent
        """
        qwidget = self.qwidget
        self.qlayout.removeWidget(self.qwidget)

        self.update_geometry(qwidget, kwargs)
        self.update_icon(qwidget, kwargs)

        for arg in kwargs:
            qwidget.setProperty(arg, kwargs.get(arg))

        self.qlayout.addWidget(qwidget)
        self.qwidget = qwidget

    def update_geometry(self, qwidget, kwargs):
        """"
        Update qwidget's geometry
        :param qwidget: QWidget to update geometry of
        :param kwargs: kwargs from update function
        """
        if 'x' in kwargs or \
           'y' in kwargs or \
           'width' in kwargs or \
           'height' in kwargs:
            x = kwargs.pop('x') if 'x' in kwargs else qwidget.x()
            y = kwargs.pop('y') if 'y' in kwargs else qwidget.y()
            width = kwargs.pop('width') if 'width' in kwargs \
                else qwidget.width()
            height = kwargs.pop('height') if 'height' in kwargs \
                else qwidget.height()

            qwidget.setGeometry(x, y, width, height)

    def update_icon(self, qwidget, kwargs):
        """"
        Update qwidget's geometry
        :param qwidget: QWidget to update icon of
        :param kwargs: kwargs from update function
        """
        if 'icon' in kwargs:
            icon = kwargs.pop('icon')
            qwidget.setIcon(QIcon(icon))
