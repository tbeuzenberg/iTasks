""" Unit test file for itasks_component """

import unittest

from unittest.mock import Mock

from itasks_components import ItasksComponent


class ItasksComponentTest(unittest.TestCase):
    """Test cases for itasks_component"""

    def test__init__(self):
        """Tests if the constructor assigns the given values properly"""

        # Assign
        qwidget = Mock()
        qgridlayout = Mock()

        # Act
        component = ItasksComponent(action_id="Action_ID", task_id="Task_ID",
                                    qwidget=qwidget, qlayout=qgridlayout)

        # Assert
        qgridlayout.addWidget.assert_called_with(qwidget)

        self.assertEqual(component.qwidget, qwidget)
        self.assertEqual(component.qlayout, qgridlayout)
        self.assertEqual(component.action_id, "Action_ID")
        self.assertEqual(component.task_id, "Task_ID")


if __name__ == '__main__':
    unittest.main()
