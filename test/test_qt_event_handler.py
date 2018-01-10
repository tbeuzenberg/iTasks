""" Unit tests for qt_event_handler.py """

# pylint: disable=R0201, C0103

import unittest

# pylint: disable=ungrouped-imports
from unittest.mock import (
    patch,
    Mock
)
# pylint: enable=ungrouped-imports

from itasks_components import ItasksComponent
from qt_event_handler import QtEventHandler


class TestQtEventHandler(unittest.TestCase):
    """ Unit test class """

    def test_button_clicked_event(self):
        """
        method: button_clicked_event
        state: button clicked
        expected_result: itasks_service.send_ui_event is called with correct data
        """
        # Assign
        itasks_service = Mock()
        qt_event_handler = QtEventHandler(itasks_service)
        qpushbutton = Mock()
        button = ItasksComponent(qpushbutton, "Ok", "2-0")

        # Act
        qt_event_handler.button_clicked_event(button)

        # Asserts
        itasks_service.send_ui_event.assert_called_once_with(
            {"instanceNo": 2, "taskNo": 0, "action": "Ok"}
        )

    @patch('PyQt5.QtWidgets.QLineEdit.text', return_value='kaas')
    def test_textbox_changed_event(self, text_function):
        """
        method: textbox_changed_event
        state: text changed
        expected_result: itasks_service.send_ui_event is called with correct data
        """
        # Assign
        itasks_service = Mock()
        qt_event_handler = QtEventHandler(itasks_service)
        qlineedit = Mock()
        qlineedit.text = text_function
        textbox = ItasksComponent(qlineedit, None, "2-1")

        # Act
        qt_event_handler.textbox_changed_event(textbox)

        # Asserts
        itasks_service.send_ui_event.assert_called_once_with(
            {"instanceNo": 2, "taskNo": 1, "edit": "v", "value": "kaas"}
        )
