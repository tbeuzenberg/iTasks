import json
import sys

from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QWidget, QLabel


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node, location):
        if location >= len(self.children):
            for i in range(0, location):
                    self.children.append(Node())
        self.children.append(node)

    def replace_child(self, node, location):
        self.children[location] = node

    def add_or_replace_child(self, node, location):
        """
        Chooses whether a node has to be added or replaced, and acts accordingly
        :param node: Node
        :param location: str
        :rtype: void
        """
        if location >= len(self.children):
            self.add_child(node, location)
        else:
            self.replace_child(node, location)

    def get_child(self, location):
        return self.children[int(location)]

    def search_node(self, location):
        if len(str(location)) == 1:
            return self.get_child(location)
        else:
            first_digit = int(str(location)[:1])
            rest = str(location)[1:]
            return self.children[first_digit].search_node(rest)

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

    def search_node(self, location):
        return self.root.search_node(location)

    def insert(self, value, location):
        node = Node(value)

        if len(location) <= 1:
            self.root.add_or_replace_child(node, int(location))
        else:
            last = location[len(location) - 1:]
            rest = location[:len(location) - 1]
            self.root.search_node(rest).add_or_replace_child(node, int(last))

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
