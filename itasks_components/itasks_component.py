from PyQt5.QtWidgets import QLayout, QWidget


class ItasksComponent:
    """
    Component which is used to cluster iTask-specific attributes.
    Used as "value" attribute in a Node.
    """
    def __init__(self, qwidget: QWidget=None, action_id=None, task_id=None, qlayout: QLayout=None):
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