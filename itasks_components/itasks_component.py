"""Itasks_component for use in a Node"""
# pylint: disable-msg=too-few-public-methods
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

    # def reset(self):
    #     self.action_id = None
    #     self.task_id = None
    #     for i in range(self.qlayout.count()):
    #         print(i)

    def update(self, **kwargs):
        pass
