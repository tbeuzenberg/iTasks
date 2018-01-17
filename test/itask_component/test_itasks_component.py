""" Unit test file for itasks_component """

import unittest

from unittest.mock import Mock, patch

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

    def test_update_text_changed(self):
        """"sdf"""
        # Assign
        data = [
            {
                "name": "text",
                "value": "itasks"
            }
        ]
        qwidget = Mock()
        qlayout = Mock()
        button = ItasksComponent(qwidget, qlayout)

        # Act
        button.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        button.qwidget.setProperty.\
            assert_called_once_with("text", "itasks")

    def test_update_icon_changed(self):
        """"sdf"""
        # Assign
        data = [
            {
                "name": "iconCls",
                "value": "accept.png"
            }
        ]
        qwidget = Mock()
        qlayout = Mock()
        icon = ItasksComponent(qwidget, qlayout)

        # Act
        icon.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        icon.qwidget.setIcon.\
            assert_called_once()

    def test_update_value_changed(self):
        """"sdf"""
        # Assign
        data = [
            {
                "name": "value",
                "value": "itasks"
            }
        ]
        qwidget = Mock()
        qlayout = Mock()
        textfield = ItasksComponent(qwidget, qlayout)

        # Act
        textfield.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        textfield.qwidget.setText. \
            assert_called_once_with("itasks")

    def test_update_hint_and_hint_type_changed(self):
        """"sdf"""
        # Assign
        data = [
            {
                "name": "hint",
                "value": "itasks"
            },
            {
                "name": "hint-type",
                "value": "valid"
            }
        ]
        qwidget = Mock()
        qlayout = Mock()
        icon = ItasksComponent(qwidget, qlayout)

        # Act
        icon.update(data)

        # Assert
        qlayout.removeWidget.assert_called_once_with(qwidget)
        qlayout.addWidget.assert_called_with(qwidget)
        icon.qwidget.setTooltip. \
            assert_called_once_with("itasks")
        icon.qwidget.setIcon. \
            assert_called_once()


if __name__ == '__main__':
    unittest.main()
