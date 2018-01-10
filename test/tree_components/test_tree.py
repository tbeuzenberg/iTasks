""" Unit test file for the tree component """
# pylint: disable=invalid-name, no-self-use

import unittest
from unittest.mock import (
    Mock,
    patch
)

from tree_components import (
    Tree,
    Node
)


class TreeTest(unittest.TestCase):
    """ Unit test class for the tree component """

    @patch('tree_components.Node.find_node')
    def test_find_node_mock(self, find_node_mock):
        """
        Test for searching a node of a tree.

        :method: find_node
        :expect: The find_node method of the root to be called with the
        search same search parameters as for the tree
        :param find_node_mock: Mocked find_node of the Node class.
        """
        # Assign
        root = Node("Root node")
        tree = Tree(root_node=root)

        # Act
        tree.find_node(index_list=[0])

        # Assert
        find_node_mock.assert_called_with(index_list=[0])

    def test_find_node_mock_with_empty_list(self):
        """
        Test for searching a node of a tree with an empty list.

        :method: find_node
        :expect: The root node to be returned
        """
        # Assign
        root = Node("Root node")
        tree = Tree(root_node=root)

        # Act
        returned_node = tree.find_node([])

        # Assert
        self.assertEqual(root, returned_node)


    def test_insert_with_one_numbered_location(self):
        """
        Test for adding a node with a single digit index list.
        When the index_list has only one item, the item should be added to the
        root node.

        :method: insert
        :state: A tree with only a root node, which has no children.
        :expect: The add_or_replace_child to be called with the right
        parameters on the given digit.
        """
        # Assign
        root = Node("Root node")
        tree = Tree(root_node=root)
        node_to_be_inserted = Node("To be inserted")
        root.add_or_replace_child = Mock()

        # Act
        tree.insert(node=node_to_be_inserted, index_list=[3])

        # Assert
        root.add_or_replace_child.assert_called_with(
            node=node_to_be_inserted,
            index=3
        )

    @patch('tree_components.Node.find_node')
    @patch('tree_components.Node.add_or_replace_child')
    def test_insert_with_two_numbered_location(self, add_or_replace_child_mock,
                                               find_node_mock):
        """
        Test for adding a node with an index list with two numbers.

        :method: insert
        :state: A tree with a root node, which has a child on index 0.
        :expect: The add_or_replace_child to be called with the right
        parameters on the given numbers.
        :param add_or_replace_child_mock: Mocked add_or_replace_child of the
        :param find_node_mock: Mocked find_node of the Node class
        Node class
        """
        # Assign
        root = Node("Root node")
        child = Node("Child node")
        root.add_or_replace_child(node=child, index=0)
        tree = Tree(root_node=root)
        find_node_mock.return_value = child
        node_to_be_inserted = Node("To be inserted")

        # Act
        tree.insert(node=node_to_be_inserted, index_list=[3, 0])

        # Assert
        find_node_mock.assert_called_with(index_list=[3])
        add_or_replace_child_mock.assert_called_with(
            node=node_to_be_inserted,
            index=0
        )

    @patch('tree_components.Node.find_node')
    @patch('tree_components.Node.add_or_replace_child')
    def test_insert_with_four_numbered_location(self,
                                                add_or_replace_child_mock,
                                                find_node_mock):
        """
        Test for adding a node with an index list with four numbers.

        :method: insert
        :state: A tree with a root node
        :expect: The add_or_replace_child to be called multiple times for every
        insert. The On the last insert it should be called with the
        correct parameters as tested in the assert.
        :param add_or_replace_child_mock: Mocked add_or_replace_child of the
        Node class
        :param find_node_mock: Mocked find_node of the Node class
        """
        # Assign
        root = Node("Root node")
        child = Node("Child node")
        root.add_or_replace_child(node=child, index=0)
        tree = Tree(root_node=root)
        find_node_mock.return_value = child
        node_to_be_inserted1 = Node("To be inserted")
        node_to_be_inserted2 = Node("To be inserted two")
        node_to_be_inserted3 = Node("To be inserted three")

        # Act
        tree.insert(node=node_to_be_inserted1, index_list=[3, 0])
        tree.insert(node=node_to_be_inserted2, index_list=[3, 0, 4])
        tree.insert(node=node_to_be_inserted3, index_list=[3, 0, 4, 8])

        # Assert
        find_node_mock.assert_called_with(index_list=[3, 0, 4])
        add_or_replace_child_mock.assert_called_with(
            node=node_to_be_inserted3,
            index=8
        )

    def test_call_print_root(self):
        """
        Test if the print function works
        :state: Tree with root node
        :method: print
        :expect: The Node print function to be called
        """
        # Assign
        root = Node("Root node")
        tree = Tree(root_node=root)

        # Act
        with patch('tree_components.Node.print', return_value="") as print_mock:
            tree.print()

        # Assert
        print_mock.assert_called()


if __name__ == '__main__':
    unittest.main()
