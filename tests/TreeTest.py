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
        root = Node()
        tree = Tree(root)
        tree.insert("Fake QWidget at position 3", "3")
        tree.insert("Fake QWidget at position 2", "2")

        self.assertNotEqual(tree.search_node("3").qwidget, tree.search_node("2").qwidget)

    def test_insert(self):
        root = Node()
        tree = Tree(root)
        tree.insert("Fake QWidget", "3")

        self.assertEqual(tree.search_node("3").qwidget, "Fake QWidget")

    def test_print(self):
        root = Node()
        tree = Tree(root)


if __name__ == '__main__':
            unittest.main()