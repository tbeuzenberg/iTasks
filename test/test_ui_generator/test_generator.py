""" Unit test file for the UIGenerator """
# pylint: disable=invalid-name, no-self-use

import sys
import unittest

from unittest.mock import Mock, call

from tree_components import Node
from ui_generator import (
    UIGenerator,
    Components
)


class TestUIGenerator(unittest.TestCase):
    """ Test cases for the UIGenerator """
    def setUp(self):
        """
        Save methods for mock reset
        """
        self.rrui = UIGenerator.read_replace_ui_instruction
        self.cor = UIGenerator.change_or_replace
        self.cc = UIGenerator.create_component
        self.rcui = UIGenerator.read_change_ui_instruction

    def tearDown(self):
        """
        Mock reset
        """
        UIGenerator.read_replace_ui_instruction = self.rrui
        UIGenerator.change_or_replace = self.cor
        UIGenerator.create_component = self.cc
        UIGenerator.read_change_ui_instruction = self.rcui

    def test_change_or_replace_replace(self):
        """
        :method:
        :state:
        :expect:
        """
        # Assign
        UIGenerator.read_change_ui_instruction = Mock()
        UIGenerator.read_replace_ui_instruction = Mock()
        node = Node("Piet-Jan Heijn")
        change = {
            "type": "replace",
            "definition": {
                "type": "Panel",
                "attributes": {
                    "height": "flex",
                    "width": "flex"
                }
            }
        }

        # Act
        UIGenerator.change_or_replace(node=node, change=change)

        # Assert
        UIGenerator.read_change_ui_instruction.assert_not_called()
        UIGenerator.read_replace_ui_instruction.assert_called_with(
            parent_node=node,
            index=0,
            replace_instruction=change["definition"]
        )

    def test_change_or_replace_change(self):
        """
        :method:
        :state:
        :expect:
        """
        # Assign
        UIGenerator.read_change_ui_instruction = Mock()
        UIGenerator.read_replace_ui_instruction = Mock()
        node = Node("Piet-Jan Heijn")
        change = {
            "type": "change",
            "attributes": [],
            "children": [
                1,
                "change",
                {
                }
            ]
        }

        # Act
        UIGenerator.change_or_replace(node=node, change=change)

        # Assert
        UIGenerator.read_replace_ui_instruction.assert_not_called()
        UIGenerator.read_change_ui_instruction.assert_called_with(
            current_node=node,
            change_instruction=change
        )

    def test_read_replace_ui_instruction(self):
        """
        :method:
        :state:
        :expect:
        """
        # Assign
        UIGenerator.create_component = Mock()
        node = Node("Piet-Jan Heijn")
        attributes = {
            "height": "flex",
            "width": "flex"
        }
        change = {
            "type": "Panel",
            "attributes": attributes,
        }
        index = 0

        Node.__new__ = Mock()
        Node.__new__.return_value = node
        Node.add_or_replace_child = Mock()

        # Act
        UIGenerator.read_replace_ui_instruction(
            parent_node=node,
            index=0,
            replace_instruction=change
        )

        UIGenerator.create_component.assert_called_with(
            component_type=change['type'],
            parent_node=node,
            index=index,
            attributes=attributes
        )
        Node.add_or_replace_child.assert_called_with(index=index, node=node)

    def test_create_component(self):
        """
        :method:
        :state:
        :expect:
        """
        component_type = "button"
        name = "Piet-Jan Heijn"
        parent_node = Node(name)
        index = 0
        attributes = {
            "height": "flex",
            "width": "flex"
        }
        button = {"button": "button"}

        Components.button = Mock()
        Components.button.return_value = button

        created_component = UIGenerator.create_component(
            component_type=component_type,
            parent_node=parent_node,
            index=index,
            attributes=attributes
        )

        Components.button.assert_called_with(
            parent=name,
            index=index,
            **attributes
        )
        self.assertEqual(button, created_component)

    def test_read_change_ui_instruction(self):
        pass





if __name__ == '__main__':
    unittest.main()
