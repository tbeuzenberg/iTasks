import json
import sys

from PyQt5.QtWidgets import (
    QPushButton,
    QMainWindow,
    QApplication,
    QWidget,
    QLabel
)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node, index):
        if index >= len(self.children):
            for i in range(0, index):
                    self.children.append(Node())
        self.children.append(node)

    def replace_child(self, node, index):
        self.children[index] = node

    def add_or_replace_child(self, node, index):
        """
        Chooses whether a node has to be added or replaced, and acts accordingly
        :param node: Node
        :param node: str
        :rtype: void
        """
        if index >= len(self.children):
            self.add_child(node=node, index=index)
        else:
            self.replace_child(node=node, index=index)

    def get_child(self, index):
        return self.children[index]

    def search_node(self, index_list):
        if len(index_list) == 1:
            return self.get_child(index=index_list[0])
        else:
            first_element = index_list[:1]
            rest = index_list[1:]
            return self.children[first_element[0]].search_node(index_list=rest)

    def print(self, prefix=""):
        if self.value is None:
            print(prefix + "None")
        else:
            print(prefix + type(self.value).__name__)

        if len(self.children) > 0:
            for i in range(0, len(self.children)):
                self.children[i].print(prefix + "- ")


class Tree:
    def __init__(self, root):
        self.root = root

    def search_node(self, index_list):
        return self.root.search_node(index_list=index_list)

    def insert(self, value, index_list):
        node = Node(value)

        if len(index_list) <= 1:
            self.root.add_or_replace_child(node=node, index=index_list[0])
        else:

            last = index_list[len(index_list) - 1:]
            rest = index_list[:len(index_list) - 1]

            self.root.search_node(index_list=rest).add_or_replace_child(node=node, index=last[0])

    def print(self):
        self.root.print()


# app = QApplication(sys.argv)
# window = QWidget()
#
# QPushButton('ergesadh', window)
# pb = QPushButton('str')
# first_button = Node(pb)
# tree = Tree(first_button)
# tree.insert(QPushButton('hoi'), "3")
# tree.insert(QPushButton('hee'), "1")
#
# tree.insert(QPushButton('hallo'), "30")
# tree.insert(QPushButton('hallo'), "305")
#
# tree.insert(QLabel('pinda'), "30")

#
# tree.print()
#
# window.show()
# sys.exit(app.exec_())

#
# def json_decode_string(str_in):
#     return json.loads(str_in)
#
#
# def json_decode_file(file_in):
#     return json.load(file_in)
