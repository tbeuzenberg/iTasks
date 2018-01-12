""" File for the application class """
import json

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout
)

from ui_generator import UIGenerator
from tree_components import(
    Tree,
    Node
)


class Application:
    """ Application out of an iTasks instruction """
    instance_trees = {}

    def __init__(self, application: QApplication, main_window: QMainWindow):
        self.__application = application
        self.__main_layout = QGridLayout()
        self.__main_window = main_window

    @property
    def qt_application(self):
        return self.__application

    @property
    def main_window(self):
        return self.__main_window

    @property
    def main_layout(self):
        return self.__main_layout

    def add_instance_tree(self, instance_id, itasks_component):
        self.instance_trees[instance_id] = Tree(root_node=Node(itasks_component))

    def get_instance_tree(self, instance_id):
        if instance_id not in self.instance_trees:
            raise IndexError()
        return self.instance_trees[instance_id].root.value

    def get_component_from_instance(self, instance_id, location):
        return self.instance_trees[instance_id].find_node(index_list=location)

    def handle_instruction(self, json_instruction):
        parsed_json = json.loads(json_instruction)
        instance = parsed_json.get("instanceNo") if "instanceNo" in json_instruction else parsed_json.get("instance")

        if instance not in self.instance_trees:
            tree = Tree(Node("Dummy")).insert(
                node=Node("Actual_data"),
                index_list=[0]
            )
            self.add_instance_tree(instance, tree)

        current_tree = self.instance_trees.get(instance)

        UIGenerator.change_or_replace(
            node=current_tree.root,
            change=parsed_json.get("change")
        )