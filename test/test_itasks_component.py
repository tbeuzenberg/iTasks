""" Unit test file for itasks_component """

import unittest

from unittest.mock import Mock

from itasks_components import ItasksComponent


class ItasksComponentTest(unittest.TestCase):
    """Test cases for itasks_component"""
    def test__init__(self):
        """Tests if the constructor assigns the given values properly"""

        #Assign
        QWidget = Mock()
        QGridLayout = Mock()
        layout = QGridLayout()
        widget = QWidget()

        #Act
        component = ItasksComponent(action_id="Action_ID", task_id="Task_ID", qwidget=widget, qlayout=layout)

        #Assert
        self.assertEqual(component.qwidget, widget)
        self.assertEqual(component.qlayout, layout)
        self.assertEqual(component.action_id, "Action_ID")
        self.assertEqual(component.task_id, "Task_ID")


if __name__ == '__main__':
    unittest.main()
