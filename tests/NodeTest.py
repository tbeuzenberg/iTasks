import unittest
import builtins
from unittest.mock import (
    call,
    Mock
)

from JSONParser import (
    Node
)


class NodeTest(unittest.TestCase):

    def test_private_add_child_one_deep(self):
        # Assign
        root = Node("Ding")
        child = Node("Ding2")

        # Act
        root.add_child(child, 3)

        # Assert
        self.assertEqual(child.value, root.children[3].value)

    def test_replace_child(self):
        # Assign/act
        root = Node("Ding")
        child = Node("Ding2")
        root.add_child(child, 3)
        child2 = Node("Ding3")
        root.replace_child(child2, 3)

        # Assert
        self.assertEqual(child2.value, root.children[3].value)

    def test_add_or_replace_child_with_replace(self):
        # Assign
        root = Node("Ding")
        node1 = Node("1")
        node2 = Node("2")
        root.add_child(node1, 0)
        root.replace_child = Mock(name="replace_child")
        root.add_child = Mock(name="add_child")

        root.add_or_replace_child(node=node2, index=5)

        root.add_child.assert_called_once_with(node=node2, index=5)
        root.replace_child.assert_not_called()

    def test_add_or_replace_child_with_add(self):
        # Assign
        root = Node("Ding")
        node1 = Node("1")
        node2 = Node("2")
        root.add_child(node1, 0)
        root.replace_child = Mock(name="replace_child")
        root.add_child = Mock(name="add_child")

        root.add_or_replace_child(node=node2, index=0)

        root.replace_child.assert_called_once_with(node=node2, index=0)
        root.add_child.assert_not_called()

    def test_get_child(self):
        # Assign
        root = Node("Ding")
        node1 = Node("1")
        root.add_child(node=node1, index=0)

        # Act
        retrieved_child = root.get_child(index=0)

        # Assert
        self.assertEqual(retrieved_child, node1)

    def test_search_node(self):
        # Assign
        node2 = Node("2")
        node3 = Node("3")
        node2.add_child(node=node3, index=2)

        node1 = Node("1")
        node1.add_child(node=node2, index=0)

        root = Node("Ding")
        root.add_child(node=node1, index=3)

        # Act
        retrieved_node1 = root.search_node([3])
        retrieved_node2 = root.search_node([3, 0])
        retrieved_node3 = root.search_node([3, 0, 2])

        # Assert
        self.assertEqual(node1, retrieved_node1)
        self.assertEqual(node2, retrieved_node2)
        self.assertEqual(node3, retrieved_node3)

    def test_print(self):
        # Assign
        builtins.print = Mock()

        node2 = Node("2")
        node3 = Node("3")
        node2.add_child(node3, 2)

        node1 = Node("1")
        node1.add_child(node2, 0)

        root = Node("Ding")
        root.add_child(node1, 3)

        # Act
        root.print()

        calls = [
            call("str"),
            call("- None"),
            call("- None"),
            call("- None"),
            call("- str"),
            call("- - str"),
            call("- - - None"),
            call("- - - None"),
            call("- - - str"),
        ]

        builtins.print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
