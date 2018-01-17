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

from application import (
    Application,
    DuplicateKeyException
)
from tree_components import Tree
from itasks_components import ItasksComponent


class TestApplication(unittest.TestCase):
    """ The class for testing the Application class """

    def setUp(self):
        """
        Creating the application all of the tests need.
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
        Test if the constructor works correctly and calls the right methods

        :method: __init__
        :state: A new application has just been made in the setUp
        :expect: setGeometry and setCentralWidget methods should have been
        called with the correct parameters.
        """

        # Assert
        self.main_window.setGeometry.assert_called_with(0, 0, 500, 500)
        self.main_window.setCentralWidget.assert_called_with(self.widget)
        self.widget.setGeometry.assert_called_with(0, 0, 500, 500)

    def test_add_instance_tree(self):
        """
        Tests if the instance tree gets added correctly.

        :method: add_instance_tree
        :state: An application with no instance tree on place 3
        :expect: The instance to be added
        """
        # Assign
        instance_id = 3
        itasks_component = Mock()

        # Act
        self.application.add_instance_tree(
            instance_id=instance_id,
            itasks_component=itasks_component
        )

        # Assert
        self.assertTrue(
            type(self.application.instance_trees.get(instance_id)),
            Tree
        )
        self.assertEqual(
            self.application.instance_trees.get(instance_id).root.value,
            itasks_component
        )

    def test_add_instance_tree_already_exists(self):
        """
        Tests if the instance tree throws an error.

        :method: add_instance_tree
        :state: An application with an instance tree on place 1
        :expect: A DuplicateKeyException to be added
        """

        # Assign
        instance_id = 1
        itasks_component = Mock()

        self.application.add_instance_tree(
            instance_id=instance_id,
            itasks_component=itasks_component
        )

        # Act & Assert
        with self.assertRaises(DuplicateKeyException):
            self.application.add_instance_tree(
                instance_id=instance_id,
                itasks_component=itasks_component
            )

    def test_get_instance_tree(self):
        """
        Test if the instance tree can be retrieved correctly.

        :method: get_instance_tree
        :state: The application has an instance on id 2
        :expect: The instance on id 2 to be retrieved correctly
        """

        # Assign
        instance_id = 2
        itasks_component = Mock()

        self.application.add_instance_tree(
            instance_id=instance_id,
            itasks_component=itasks_component
        )

        # Act
        tree = self.application.get_instance_tree(instance_id=instance_id)

        # Assert
        self.assertEqual(itasks_component, tree.root.value)

    def test_get_instance_tree_throws_index_error(self):
        """
        Test if the instance tree retrieving throws an index error.

        :method: get_instance_tree
        :state: An application with no instance on id 6
        :expect: The get_instance_tree to throw an IndexError due to the
        instance that cannot be found
        """
        with self.assertRaises(IndexError):
            self.application.get_instance_tree(instance_id=6)

    @patch("itasks_components.itasks_component.ItasksComponent.__new__",
           return_value={"ItasksComponent", "ItasksComponent"}
           )
    @patch("application.application.Application.get_instance_tree")
    @patch("application.application.Application.add_instance_tree")
    def test_get_or_create_instance_doesnt_exist(self, add_instance_tree_mock,
                                                 get_instance_tree_mock,
                                                 itasks_component_mock):
        """
        Test for calling the correct methods with only an instanceid, and no
        instance on id 5

        :method: get_or_create_instance
        :state: An application with no instance on id 5
        :expect: add_instance_tree and the get_instance_tree to be called with
        id 5 and a generated component
        """
        itasks_component = {"ItasksComponent", "ItasksComponent"}
        itasks_component_2 = {"ItasksComponent2", "ItasksComponent2"}

        get_instance_tree_mock.return_value = itasks_component_2

        returned_item = self.application.get_or_create_instance(5)

        add_instance_tree_mock.assert_called_with(5, itasks_component)
        get_instance_tree_mock.assert_called_with(5)

        self.assertEqual(returned_item, itasks_component_2)

    @patch("application.application.Application.get_instance_tree")
    def test_get_or_create_instance_exists(self, get_instance_tree_mock):
        """
        Test for calling the correct methods with only an instanceid, but an
        instance on id 5

        :method: get_or_create_instance
        :state: An application with an instance on id 5
        :expect: only the get_instance to be called with the correct id.
        """
        itasks_component = {"ItasksComponent", "ItasksComponent"}

        get_instance_tree_mock.return_value = itasks_component

        self.application.instance_trees[7] = "test"

        with patch("application.application.Application.add_instance_tree") \
                as add_instance:
            returned_item = self.application.get_or_create_instance(7)
            add_instance.assert_not_called()

        get_instance_tree_mock.assert_called_with(7)
        self.assertEqual(returned_item, itasks_component)

    @patch("json.loads")
    @patch("ui_generator.ui_generator.UIGenerator.change_or_replace")
    @patch("application.application.Application.get_or_create_instance")
    def test_handle_instruction(self, get_or_create_mock, component_mock,
                                json_loads_mock):
        """
        Test for handling a json instruction correctly.

        :method: handle_instruction
        :state: A json instruction received by the iTasks server
        :expect: The following methods to be called: json.loads,
        get_or_create_instance and UIGenerator.change_or_replace with the
        correct parameters read from the inputted json.
        """

        # Assign
        json_instruction = '{"instanceNo": 5, "change": ' \
                           '{"type": "button", "attributes": ' \
                           '{"color": "red"}}}'

        parsed_change = {
            "type": "button",
            "attributes": {
                "color": "red"
            }
        }

        parsed_json = {
            "instanceNo": 5,
            "change": parsed_change
        }

        json_loads_mock.return_value = parsed_json
        node = {"Node": "Node"}
        get_or_create_mock.return_value = Tree(root_node=node)

        # Act
        self.application.handle_instruction(json_instruction=json_instruction)

        # Assert
        json_loads_mock.assert_called_with(json_instruction)
        get_or_create_mock.assert_called_with(parsed_json['instanceNo'])
        component_mock.assert_called_with(node=node, change=parsed_change)
