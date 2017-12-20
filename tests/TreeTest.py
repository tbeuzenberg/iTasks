import unittest
from unittest.mock import (
    call,
    Mock
)

from JSONParser import (
    Tree,
    Node
)


class TreeTest(unittest.TestCase):

    def test_search_node(self):
        # Assign
        root = Node("")
        root.search_node = Mock(name="search_node")
        tree = Tree(root)

        # Act
        tree.search_node("0")

        # Assert
        root.search_node.assert_called_with("0")

    def test_insert_with_single_digit_location(self):
        root = Node("Fake node")
        tree = Tree(root)
        to_be_added = Node("New node")

        tree.root.add_or_replace_child = Mock(name="add_or_replace_child")

        Node.__new__ = Mock()
        Node.__new__.return_value = {"AA": "AAA"}

        tree.insert(to_be_added, "3")

        tree.root.add_or_replace_child.assert_called_with({"AA": "AAA"}, 3)

    def test_insert_with_double_digit_location(self):
        # Assign
        root = Node("Fake root node")
        child = Node("Fake child node")
        root.add_or_replace_child(child, 0)
        tree = Tree(root)
        to_be_added = Node("New node")
        root.add_or_replace_child = Mock(name="root_add_or_replace_child")
        child.add_or_replace_child = Mock(name="child_add_or_replace_child")
        tree.root.search_node = Mock(name="search_node")

        # Act
        tree.root.search_node.return_value = child

        Node.__new__ = Mock()
        Node.__new__.return_value = {"AA": "AAA"}

        tree.insert(to_be_added, "30")

        # Assert
        tree.root.search_node.assert_called_with("3")
        child.add_or_replace_child.assert_called_with({"AA": "AAA"}, 0)
        root.add_or_replace_child.assert_not_called()

    def test_print(self):
        root = Node()
        tree = Tree(root)


if __name__ == '__main__':
    unittest.main()
