"""Itasks_component for use in a Node"""
# pylint: disable-msg=too-few-public-methods


class ItasksComponent:
    """
    Component which is used to cluster iTask-specific attributes.
    Used as "value" attribute in a Node.
    """
    def __init__(self, qwidget, qlayout, action_id=None, task_id=None):
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

        self.qlayout.addWidget(self.qwidget)
