""" Unit tests for qt_event_handler.py """

# pylint: disable=R0201, C0103

import unittest

# pylint: disable=ungrouped-imports
from unittest.mock import (
    patch,
    Mock
)
# pylint: enable=ungrouped-imports
from itasks import ItasksService
from itasks_components import ItasksComponent
from qt_event_handler import QtEventHandler


class TestQtEventHandler(unittest.TestCase):
    """ Unit test class """

    @patch('itasks.itasks_service.ItasksService')
    def test_button_cl1icked_event(self, itasks_service):
        """
        method: button_clicked_event
        state: button clicked
        expected_result: itasks_service.send_ui_event called with correct data
        """
        # Assign
        qpushbutton = Mock()
        button = Mock()
        button.qwidget = qpushbutton
        button.action_id = "Ok"
        button.task_id = "2-0"

        # Act
        QtEventHandler.button_clicked_event(button)

        # Asserts
        itasks_service._ItasksService__instance.send_ui_event.\
            assert_called_once_with(
            {
                "instanceNo": 2,
                "taskNo": 0,
                "action": "Ok"
            }
        )

    @patch('itasks.itasks_service.ItasksService')
    @patch('PyQt5.QtWidgets.QLineEdit.text', return_value='kaas')
    def test_textbox_changed_event(self, text_function, itasks_service):
        """
        method: textbox_changed_event
        state: text changed
        expected_result: itasks_service.send_ui_event called with correct data
        """
        # Assign
        qlineedit = Mock()
        qlineedit.text = text_function
        textbox = Mock()
        textbox.qwidget = qlineedit
        textbox.task_id = "2-1"
        textbox.editor_id = "v"

        # Act
        QtEventHandler.textbox_changed_event(textbox)

        # Asserts
        itasks_service._ItasksService__instance.send_ui_event.\
            assert_called_once_with(
                {
                    "instanceNo": 2,
                    "taskNo": 1,
                    "edit": "v",
                    "value": "kaas"
                }
            )


if __name__ == '__main__':
    unittest.main()
