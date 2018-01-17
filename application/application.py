""" File for the application class """
import json

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QWidget
)

from itasks_components import ItasksComponent

from ui_generator import UIGenerator
from tree_components import (
    Tree,
    Node
)


class Application:
    """
    application out of an iTasks instruction
    Has an instance_trees properties. These are synced to the iTasks instances
    running on the iTasks server. This way we can nest different instances and
    still reach them by only their id.
     """
    instance_trees = {}

    def __init__(self, application, grid_layout=None,
                 widget=None, main_window=None):
        """
        Initialisation of a QT application, based on an iTasks specification.
        According to PyQT, there has to be an application and a mainwindow.
        Below this, there has to be a widget with a "mainlayout", on which all
        layouts can be added.
        :param application: The application that has to be ran.
        """

        self.__application = application

        # Create if they aren't passed through as parameters
        self.__main_layout = grid_layout if grid_layout else QGridLayout()
        self.__main_widget = widget if widget else QWidget()
        self.__main_window = main_window if main_window else QMainWindow()

        # Set some base properties
        self.__main_window.setGeometry(0, 0, 500, 500)
        self.__main_widget.setGeometry(0, 0, 500, 500)
        self.__main_window.setCentralWidget(self.__main_widget)

    @property
    def qt_application(self):
        """
        The property of the application that has to be added according to PyQt.
        :rtype: QApplication
        """
        return self.__application

    @property
    def main_layout(self):
        """
        The property of the layout that has to be added according to PyQt.
        :rtype: QGridLayout
        """
        return self.__main_layout

    @property
    def main_window(self):
        """
        The property of the main window that has to be added according to PyQt.
        :rtype: QMainWindow
        """
        return self.__main_window

    @property
    def main_widget(self):
        """
        The property of the main widget that has to be added according to PyQt.
        :rtype: QWidget
        """
        return self.__main_widget

    def add_instance_tree(self, instance_id, itasks_component):
        """
        Add an instance tree to the dictionary containing them. Creates the
        tree and the root node.
        :param instance_id: The ID the tree has to be saved under
        :param itasks_component: The value of the root node.
        :rtype: void
        """
        tree = Tree(root_node=Node(itasks_component))
        self.instance_trees[instance_id] = tree

    def get_instance_tree(self, instance_id):
        """
        Get the instance tree of the dictionary.
        :param instance_id: The ID of the instance you want to get.
        :rtype: Tree
        """
        if instance_id not in self.instance_trees:
            raise IndexError()
        return self.instance_trees[instance_id]

    def handle_instruction(self, json_instruction):
        """
        Read the iTasks json and determine if you received a known or an unknown
        instance. Create or get the instance according to that.
        Call the UIGenerator with the "change"-part of the JSON and the tree.
        :param json_instruction: The instruction received from the iTasks server
        :rtype: void
        """
        parsed_json = json.loads(json_instruction)

        # This is dependent on the iTasks version you use.
        # TODO: remove.
        if "instanceNo" in json_instruction:
            instance = parsed_json.get("instanceNo")
        else:
            instance = parsed_json.get("instance")

        if instance not in self.instance_trees:
            component = ItasksComponent(
                qwidget=self.main_widget,
                qlayout=self.main_layout,
                main=True
            )
            self.add_instance_tree(instance, component)

        current_tree = self.instance_trees.get(instance)

        UIGenerator.change_or_replace(
            node=current_tree.root,
            change=parsed_json.get("change")
        )
