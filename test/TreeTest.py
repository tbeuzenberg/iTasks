import unittest
from unittest.mock import (
    patch
)

from TreeComponents import (
    Tree,
    Node
)


class TreeTest(unittest.TestCase):

    @patch('JSONParser.Node.search_node')
    def test_search_node(self, search_node_mock):
        """

        :param search_node_mock:
        :return:
        """
        # Assign
        root = Node()
        tree = Tree(root=root)

        # Act
        tree.search_node(index_list=[0])

        # Assert
        search_node_mock.assert_called_with(index_list=[0])

    @patch('JSONParser.Node.add_or_replace_child')
    def test_insert_with_single_digit_location(self, add_or_replace_child_mock):
        # Assign
        root = Node()
        tree = Tree(root=root)
        to_be_added = Node()

        # Act
        with patch('JSONParser.Node.__new__', return_value={"AA": "AAA"}):
            tree.insert(value=to_be_added, index_list=[3])

        # Assert
        add_or_replace_child_mock.assert_called_with(node={"AA": "AAA"}, index=3)

    @patch('JSONParser.Node.search_node')
    @patch('JSONParser.Node.add_or_replace_child')
    def test_insert_with_double_digit_location(self, add_or_replace_child_mock, search_node_mock):
        # Assign
        root = Node()
        child = Node()
        root.add_child(node=child, index=0)
        tree = Tree(root=root)
        search_node_mock.return_value = child

        # Act
        with patch('JSONParser.Node.__new__', return_value={"AA": "AAA"}):
            tree.insert(value="Node name", index_list=[3, 0])

        # Assert
        search_node_mock.assert_called_with(index_list=[3])
        add_or_replace_child_mock.assert_called_with(node={"AA": "AAA"}, index=0)


if __name__ == '__main__':
    unittest.main()
