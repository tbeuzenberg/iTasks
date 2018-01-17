""" Unit test file for the node component """
# pylint: disable=invalid-name, no-self-use

import builtins
import unittest

from unittest.mock import (
    call,
    Mock
)

from tree_components import Node


class TestNode(unittest.TestCase):
    """ Test cases for the Node component """

    def test_add_child(self):
        """
        Test for adding a child to a node

        :method: add_child
        :state: A tree with only a root node, which has no children.
        :expect: The root node to have one valid child on position 3
        """
        # Assign
        root = Node("Root node")
        child = Node("Child node")

        # Act
        root.add_or_replace_child(node=child, index=3)

        # Assert
        self.assertEqual(child.value, root.children[3].value)

    def test_add_child_two_items(self):
        """
        Test for adding two children to a node

        :method: add_child:
        :state: A tree with only a root node, which has no children
        :expect: The root node to have two valid children, respectively on
        index 3 and 5
        """
        # Assign
        root = Node("Root node")
        child1 = Node("Child node 1")
        child2 = Node("Child node 2")

        # Act
        root.add_or_replace_child(node=child1, index=3)
        root.add_or_replace_child(node=child2, index=5)

        # Assert
        self.assertEqual(len(root.children), 6)
        self.assertEqual(root.children[3], child1)
        self.assertEqual(root.children[5], child2)

    def test_add_child_invalid_nodes(self):
        """
        Test for adding a children to a node and invalid nodes get created

        :method: add_or_replace_child:
        :state: A tree with only a root node, which has no children
        :expect: The root node to have one valid child on index 3, and three
        invalid children on index 0, 1 and 2
        """
        # Assign
        root = Node("Root node")
        child1 = Node("Child node 1")

        # Act
        root.add_or_replace_child(node=child1, index=3)

        # Assert
        self.assertFalse(root.children[0].valid)
        self.assertFalse(root.children[1].valid)
        self.assertFalse(root.children[2].valid)
        self.assertTrue(root.children[3].valid)

    def test_replace_child(self):
        """
        Test for replacing a child of a node

        :method: add_or_replace_child
        :state: A root node with a child
        :expect: The child to be replaced with another child
        """
        # Assign
        root = Node("Root node")
        child = Node("Child node")
        root.add_or_replace_child(child, 3)
        child2 = Node("Child two node")

        # Act
        root.add_or_replace_child(child2, 3)

        # Assert
        self.assertEqual(child2.value, root.children[3].value)

    def test_get_child_child_exists(self):
        """
        Test for recieving a child with existing child

        :method: get_child
        :state: A root node with one child on position 0
        :expect: The child with index 0 gets called
        """
        # Assign
        root = Node("Root node")
        node1 = Node("Child node 1")
        root.add_or_replace_child(node=node1, index=0)

        # Act
        retrieved_child = root.get_child(index=0)

        # Assert
        self.assertEqual(retrieved_child, node1)

    def test_get_child_child_doesnt_exist(self):
        """
        Test for recieving a child with nonexisting child

        :method: get_child
        :state: A root node with one child on position 0
        :expect: The child with index 1 gets called and an error gets raised
        """
        # Assign
        root = Node("Root node")
        node1 = Node("Child node 1")
        root.add_or_replace_child(node=node1, index=0)

        # Act & Assert
        with self.assertRaises(IndexError):
            root.get_child(index=1)

    def test_find_node(self):
        """
        Test for searching and finding through the children of a node with
        location specified.

        :method: find_node
        :state: A root node with a child on index 3. This child has a child on
        index 0, which again has a child on index 2.
        :expect: to find a node on location 3 of root, 3, 0 of root and on
        3, 0, 2 of root.
        """
        # Assign
        node2 = Node("Child node 2")
        node3 = Node("Child node 3")
        node2.add_or_replace_child(node=node3, index=2)

        node1 = Node("Child node 1")
        node1.add_or_replace_child(node=node2, index=0)

        root = Node("Root node")
        root.add_or_replace_child(node=node1, index=3)

        # Act
        retrieved_node1 = root.find_node([3])
        retrieved_node2 = root.find_node([3, 0])
        retrieved_node3 = root.find_node([3, 0, 2])

        # Assert
        self.assertEqual(node1, retrieved_node1)
        self.assertEqual(node2, retrieved_node2)
        self.assertEqual(node3, retrieved_node3)

    def test_find_node_out_of_range(self):
        """
        Try to find a node that doesn't exist.

        :method: find_node
        :state: A root node with a child node on index 3, try to find a node
        on index 4
        :expect: that an IndexError gets raised due to the fact there is no
        node on index 4
        """
        # Assign
        node1 = Node("Child node 1")

        root = Node("Root node")
        root.add_or_replace_child(node1, 3)

        # Act & Assert
        with self.assertRaises(IndexError):
            root.find_node(index_list=[4])

    def test_find_node_not_valid(self):
        """
        Try to find a node that is not valid

        :method: find_node
        :state: A root node with an invalid child node on index 3. Find
        node on index 3
        :expect: that an IndexError gets raised due to the fact there is no
        valid node on index 3
        """
        # Assign
        node1 = Node(None, valid=False)

        root = Node("Root node")
        root.add_or_replace_child(node1, 3)

        # Act & Assert
        with self.assertRaises(IndexError):
            root.find_node(index_list=[3])

    def test_print(self):
        """
        Print the tree of the root node
        :method: print
        :state: A root node with a child1 node on index 3. Child1 has a child2
        on index 0. Child2 has a child3 on index 2.
        :expect: The following tree to be printed:
        str
        - None
        - None
        - None
        - str
        - - str
        - - - None
        - - - None
        - - - str
        """
        # Assign
        builtins.print = Mock()

        node2 = Node("Child node 2")
        node3 = Node("Child node 3")
        node2.add_or_replace_child(node3, 2)

        node1 = Node("Child node 1")
        node1.add_or_replace_child(node2, 0)

        root = Node("Root node")
        root.add_or_replace_child(node1, 3)

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

        # Assert
        builtins.print.assert_has_calls(calls)

    def test_has_child_child_not_found(self):
        # Assign
        node1 = Node("Node 1")
        node2 = Node("Node 2")

        node1.add_or_replace_child(node2, 1)

        # Act
        bool = node1.has_child(0)

        # Assert
        self.assertFalse(bool)

    # def test_has_child_index_out_of_range(self):
    #
    #
    # def test_has_child_index_equal_to_children_length(self):
    #
    # def test_has_child_child_found(self):


if __name__ == '__main__':
    unittest.main()
