"""Unit test file for the component method aggregate"""
# pylint: disable=unused-argument, protected-access
# pylint: disable=no-member, no-member, no-self-use, invalid-name
import unittest
from unittest.mock import Mock, patch

from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QBoxLayout, QGridLayout

from itasks_components import ItasksComponent
from ui_generator.components import Components


class TestComponents(unittest.TestCase):
    """Test cases for the component method aggregate class"""

    def setUp(self):
        """
        Sets up code before running the tests
        """
        self.boxlayout_addwidget = patch('PyQt5.QtWidgets.QBoxLayout.addWidget',
                                         return_value=None)
        self.gridlayout_addwidget = patch(
            'PyQt5.QtWidgets.QGridLayout.addWidget',
            return_value=None)
        self.qlabel = patch('PyQt5.QtWidgets.QLabel.__new__',
                            return_value=Mock())
        self.qlineedit = patch('PyQt5.QtWidgets.QLineEdit.__new__',
                               return_value=Mock())
        self.qwidget = patch('PyQt5.QtWidgets.QWidget.__new__',
                             return_value=Mock())
        self.boxlayout_addwidget.start()
        self.gridlayout_addwidget.start()
        self.qlabel.start()
        self.qlineedit.start()
        self.qwidget.start()

    def tearDown(self):
        """
        Removes patches after running all tests in this file
        """
        self.boxlayout_addwidget.stop()
        self.gridlayout_addwidget.stop()
        self.qlabel.stop()
        self.qlineedit.stop()
        self.qwidget.stop()

    def test_private_set_margins_default_parameters(self):
        """
        Tests the private __set_margins function,
        asserts if it calls setContentMargins
        correctly when no parameters
        are given besides the button itself
        """
        # Assign)
        button = Mock()

        # Act
        Components._Components__set_margins(button)

        # Assert
        button.setContentsMargins.assert_called_with(0, 0, 0, 0)

    def test_private_set_margins_custom_parameters(self):
        """
        Tests the private __set_margins function,
        asserts if it calls setContentsMargins correctly
        when all parameters are filled
        """
        # Assign)
        button = Mock()

        # Act
        Components._Components__set_margins(button, 1, 2, 3, 4)

        # Assert
        button.setContentsMargins.assert_called_with(1, 2, 3, 4)

    @patch('PyQt5.QtWidgets.QPushButton.sizeHint', return_value=QSize(1, 1))
    def test_private_set_geometry_default_parameters(self, sizehint):
        """
        Tests the private __set_geometry function,
        asserts if it calls the setGeometry function correctly
        when no parameters are passed aside from the button itself
        :param sizehint: the patched sizeHint function
        """
        # Assign
        button = Mock()
        button.sizeHint = sizehint

        # Act
        Components._Components__set_geometry(button)

        # Assert
        button.setGeometry.assert_called_with(0, 0, 1, 1)

    @patch('PyQt5.QtWidgets.QPushButton.sizeHint', return_value=QSize(3, 4))
    def test_private_set_geometry_custom_parameters(self, sizehint):
        """
        Tests the private __set_geometry function,
        asserts if it calls the setGeometry function correctly
        when custom parameters are passed.
        :param sizehint: the patched sizeHint function
        """
        # Assign
        button = Mock()
        button.sizeHint = sizehint

        # Act
        Components._Components__set_geometry(button, 1, 2, 3, 4)

        # Assert
        button.setGeometry.assert_called_with(1, 2, 3, 4)

    def test_private_nest_layout(self):
        """
        Tests the private __nest_layout function,
        asserts if the child is nested correctly into the child
        """
        # Assign
        layout = QBoxLayout(0)
        parent_layout = QGridLayout()
        parent = ItasksComponent(qwidget=Mock(), qlayout=parent_layout,
                                 main=True)
        # Act
        Components._Components__nest_layout(parent=parent, layout=layout)

        # Assert
        self.assertEqual(parent_layout.children()[0], layout)

    @patch('PyQt5.QtWidgets.QWidget.sizeHint', return_value=QSize(1, 1))
    def test_buttonbar(self, sizehint):
        """
        Tests the buttonbar method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget function
        :param sizehint: patched sizehint function
        :param qwidget: patched qwidget constructor
        :return:
        """
        # Assign
        q_w = QtWidgets.QWidget()
        q_w.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        q_l.addWidget = self.boxlayout_addwidget
        parent = ItasksComponent(qwidget=q_w, qlayout=q_l)

        # Act
        button_bar = Components.buttonbar(parent=parent, index=0)

        # Assert
        self.assertEqual(type(button_bar), ItasksComponent)
        self.assertEqual(type(button_bar.qlayout), QBoxLayout)
        # QWidget assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('PyQt5.QtWidgets.QPushButton.setIcon', return_value=None)
    @patch('PyQt5.QtWidgets.QPushButton.sizeHint', return_value=QSize(1, 1))
    def test_button(self, sizehint, seticon):
        """
        Tests the button method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param sizehint: patched sizehint method
        :param seticon: patched seticon method
        :param qpushbutton: patched QPushButton constructor
        :return:
        """
        # Assign
        q_b = QtWidgets.QPushButton()
        q_b.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_b, qlayout=q_l)

        # Act
        button = Components.button(parent=parent, index=0)

        # Assert
        button.qwidget.setText.assert_called_with("")
        button.qwidget.setEnabled.assert_called_with(True)
        button.qwidget.setIcon.assert_called()
        self.assertEqual(type(button), ItasksComponent)
        self.assertEqual(type(button.qlayout), QGridLayout)
        # QPushButton assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('PyQt5.QtWidgets.QWidget.sizeHint', return_value=QSize(1, 1))
    def test_container(self, sizehint):
        """
        Tests the container method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param sizehint: patched sizehint method
        :param qwidget: patched QWidget constructor
        :return:
        """
        # Assign
        q_b = QtWidgets.QWidget()
        q_b.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_b, qlayout=q_l)

        # Act
        container = Components.container(parent=parent, index=0)

        # Assert
        self.assertEqual(type(container), ItasksComponent)
        self.assertEqual(type(container.qlayout), QGridLayout)
        # QWidget assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('PyQt5.QtWidgets.QLabel.sizeHint', return_value=QSize(1, 1))
    def test_icon(self, sizehint):
        """
        Tests the icon method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param sizehint: patched sizehint method
        :param qlabel: patched QLabel constructor
        :return:
        """
        # Assign
        q_lb = QtWidgets.QLabel()
        q_lb.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_lb, qlayout=q_l)

        # Act
        icon = Components.icon(parent=parent, index=0, iconCls="icon")

        # Assert
        self.assertEqual(type(icon), ItasksComponent)
        self.assertEqual(type(icon.qlayout), QGridLayout)
        # QLabel assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('PyQt5.QtWidgets.QLineEdit.sizeHint', return_value=QSize(1, 1))
    def test_textfield(self, sizehint):
        """
        Tests the textfield method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param sizehint: patched sizehint method
        :param qlineedit: patched qlineedit constructor
        :return:
        """
        # Assign
        q_le = QtWidgets.QLineEdit()
        q_le.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_le, qlayout=q_l)

        # Act
        textfield = Components.textfield(parent=parent, index=0,
                                         value="textfield")

        # Assert
        textfield.qwidget.setText.assert_called_with("textfield")
        textfield.qwidget.setToolTip.assert_called_with("")
        self.assertEqual(type(textfield), ItasksComponent)
        self.assertEqual(type(textfield.qlayout), QGridLayout)
        # QLineEdit assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('PyQt5.QtWidgets.QLabel.sizeHint', return_value=QSize(1, 1))
    def test_textview(self, sizehint):
        """
        Tests textview method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param sizehint: patched sizehint method
        :param qlabel: patched qlabel constructor
        :return:
        """
        # Assign
        q_lb = QtWidgets.QLabel()
        q_lb.sizeHint = sizehint
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_lb, qlayout=q_l)

        # Act
        textview = Components.textview(parent=parent, index=0, value="textview")

        # Assert
        textview.qwidget.setText.assert_called_with("textview")
        self.assertEqual(type(textview), ItasksComponent)
        self.assertEqual(type(textview.qlayout), QGridLayout)
        # QLabel assignment cannot be tested, as the class
        # needs to be mocked to make the test work

    @patch('ui_generator.components.Components.container', return_value=Mock())
    def test_panel(self, container):
        """
        Tests the panel method. Tests if it returns an ItasksComponent,
        and if the QLayout in the ItasksComponent is the expected type.
        :param addwidget: patched addwidget method
        :param container: patched container method
        :param qwidget: patched QWidget constructor
        :return:
        """
        # Assign
        q_w = QtWidgets.QWidget()
        q_l = QtWidgets.QGridLayout()
        parent = ItasksComponent(qwidget=q_w, qlayout=q_l)

        # Act
        Components.panel(parent=parent, index=0)

        # Assert
        Components.container.assert_called_with(parent=parent, index=0)
