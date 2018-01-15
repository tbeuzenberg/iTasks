""" File for testing the application """
import unittest

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget
)

from unittest.mock import (
    Mock,
    patch
)

from application import Application


class TestApplication(unittest.TestCase):

    def setUp(self):
        """

        :return:
        """
        self.q_application = Mock(spec=QApplication)
        self.grid_layout = Mock(spec=QGridLayout)
        self.widget = Mock(spec=QWidget)
        self.main_window = Mock(spec=QMainWindow)

        self.application = Application(
            application=self.q_application,
            grid_layout=self.grid_layout,
            widget=self.widget,
            main_window=self.main_window,
        )

    def test_create_application(self):
        """
        Test if the constructor creates all correct
        :method:
        :state:
        :expect:
        :return:

        """
        self.main_window.setGeometry.assert_called_with(0, 0, 500, 500)
        self.main_window.setCentralWidget.assert_called_with(self.widget)
        self.widget.setGeometry.assert_called_with(0, 0, 500, 500)

    def test_add_instance_tree(self):
        """

        :return:
        """
        self.application.
