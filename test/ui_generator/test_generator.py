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


class UIGeneratorTest(unittest.TestCase):
    """ Test cases for the UIGenerator """

    def setUp(self):
        self.ui_generator = UIGenerator(QApplication(sys.argv))
        self.test_widget = QWidget()
        self.ui_generator.add_widget(itasks_id=1, widget=self.test_widget)


    def test_add_widget(self):

        # Assign
        test_widget_two = QWidget()

        # Act
        self.ui_generator.add_widget(itasks_id=10, widget=test_widget_two)

        # Assert
        self.assertEqual(self.ui_generator.frame_widgets.get(10).root.value, test_widget_two)

    def test_get_widget(self):

        # Assign

        # Act
        retrieved_widget = self.ui_generator.get_widget(itasks_id=1)

        # Assert
        self.assertEqual(self.test_widget, retrieved_widget)


