""" Unit test file for itasks_component """

import unittest

from unittest.mock import Mock, patch

from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel

from itasks_components import ItasksComponent
from tree_components import Node


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

    def test_update_button_changed(self):
        """
        method: update
        state: button changed
        expected_result: button.qwidget.setText called with 'itasks'
        """
        # Assign
        data = [
            {
                "name": "text",
                "value": "itasks"
            }
        ]
        qwidget = Mock(spec=QPushButton)
        qlayout = Mock()
        button = ItasksComponent(qwidget, qlayout)

        # Act
        button.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        button.qwidget.setText.\
            assert_called_once_with("itasks")

    def test_update_icon_changed(self):
        """
        method: update
        state: icon changed
        expected_result: icon.qwidget.setText called with correct html for icon
        """
        # Assign
        data = [
            {
                "name": "iconCls",
                "value": "accept"
            }
        ]
        qwidget = Mock(spec=QLabel)
        qlayout = Mock()
        icon = ItasksComponent(qwidget, qlayout)

        # Act
        icon.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        icon.qwidget.setText.assert_called_once_with(
            "<html><img src='icons/accept.png'></html>"
        )

    def test_update_textfield_changed(self):
        """
        method: update
        state: textfield changed
        expected_result: textfield.qwidget.setText called with 'itasks'
        """
        # Assign
        data = [
            {
                "name": "value",
                "value": "itasks"
            }
        ]
        qwidget = Mock(spec=QLineEdit)
        qlayout = Mock()
        textfield = ItasksComponent(qwidget, qlayout)

        # Act
        textfield.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        textfield.qwidget.setText. \
            assert_called_once_with("itasks")

    def test_reset_qwidget_hidden(self):
        """
        method: reset
        state: itasks_component has at least 1 child
        expected_result: qwidget.hide called
        """
        # Assign
        qwidget = Mock()
        qlayout = Mock()
        itasks_component = ItasksComponent(qwidget, qlayout)

        # Act
        itasks_component.reset([Node("test")])

        # Assert
        qwidget.hide.assert_called_once()

    def test_reset_no_children(self):
        """
        method: reset
        state: itasks_component has no children
        expected_result: qwidget.hide not called
        """
        # Assign
        qwidget = Mock()
        qlayout = Mock()
        itasks_component = ItasksComponent(qwidget, qlayout)

        # Act
        itasks_component.reset([])

        # Assert
        qwidget.hide.assert_not_called()


if __name__ == '__main__':
    unittest.main()
