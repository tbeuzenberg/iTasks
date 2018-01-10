""" Unit test file for the UIGenerator """
# pylint: disable=invalid-name, no-self-use

import sys
import unittest

from unittest.mock import Mock

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)

from ui_generator import UIGenerator


class TestUIGenerator(unittest.TestCase):
    """ Test cases for the UIGenerator """

    def setUp(self):

        application = Mock()
        widget = Mock()
        self.ui_generator = UIGenerator(application)
        self.test_widget = widget
        self.ui_generator.add_widget(itasks_id=1, widget=self.test_widget)

    def test_add_widget(self):

        widget = Mock()

        # Assign
        test_widget_two = widget

        # Act
        self.ui_generator.add_widget(itasks_id=10, widget=test_widget_two)

        # Assert
        self.assertEqual(self.ui_generator.frame_widgets.get(10).root.value,
                         test_widget_two)

    def test_get_widget(self):

        # Assign

        # Act
        retrieved_widget = self.ui_generator.get_widget(itasks_id=1)

        # Assert
        self.assertEqual(self.test_widget, retrieved_widget)


if __name__ == '__main__':
    unittest.main()
