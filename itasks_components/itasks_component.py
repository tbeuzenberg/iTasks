from PyQt5.QtWidgets import (
    QWidget,
    QLayout
)


class ItasksComponent:

    def __init__(self, qwidget: QWidget=None, action_id=None, qlayout: QLayout=None):
        self.action_id = action_id
        self.widget = qwidget
        self.layout = qlayout