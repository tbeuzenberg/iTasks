from PyQt5.QtWidgets import (
    QWidget,
    QLayout
)
from ui_generator import components


class ItasksComponent:

    def __init__(self, qwidget=None, action_id=None, task_id=None, qlayout: QLayout=None):
        self.action_id = action_id
        self.task_id = task_id
        self.qwidget = qwidget
        self.qlayout = qlayout
