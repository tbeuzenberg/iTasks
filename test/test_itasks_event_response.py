""" Unit tests for functions button_clicked_event() and textbox_changed_event() in main.py """

# pylint: disable=R0201, C0103

import unittest

# pylint: disable=ungrouped-imports
from unittest.mock import (
    patch,
    Mock
)
# pylint: enable=ungrouped-imports
from PyQt5.QtWidgets import QPushButton
from itasks_components import ItasksComponent
from qt_event_handler import QtEventHandler


class TestItasksEventResponse(unittest.TestCase):
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
        button = ItasksComponent(QPushButton("Ok"), "Ok", "2-0")

        # Act
        qt_event_handler.button_clicked_event(button)

        self.assertTrue(True)
        # Assert
        itasks_service.send_ui_event.assert_called_once_with(
            {"instanceNo": 2, "taskNo": 0, "action": "Ok"}
        )
