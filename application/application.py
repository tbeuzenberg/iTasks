""" File for the application class """
import json
import queue

from PyQt5.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QWidget
)

from application.exceptions import DuplicateKeyException
from itasks import ItasksService
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
    __instance_trees = {}
    temp_start_palindrome = 0

    def __init__(self, application, grid_layout=None,
                 widget=None, main_window=None):
        """
        Initialisation of a QT application, based on an iTasks specification.
        According to PyQT, there has to be an application and a mainwindow.
        Below this, there has to be a widget with a "mainlayout", on which all
        layouts can be added.
        :param QApplication application:
        :param QGridLayout grid_layout:
        :param QWidget grid_layout:
        :param QMainWindow grid_layout:
        """

        self.__application = application
        self.callback_queue = queue.Queue()

        # Start a new itasks session
        self.itasks_service = ItasksService()
        self.itasks_service.start_server()
        self.itasks_service.new_session(self.new_session_callback)

        # Create if they aren't passed through as parameters
        self.__main_layout = grid_layout if grid_layout else QGridLayout()
        self.__main_widget = widget if widget else QWidget()
        self.__main_window = main_window if main_window else QMainWindow()

        # Set some base properties
        self.__main_window.setGeometry(0, 0, 500, 500)
        self.__main_widget.setGeometry(0, 0, 500, 500)
        self.__main_window.setCentralWidget(self.__main_widget)
        self.__main_window.closeEvent = self.close_event

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
    def instance_trees(self):
        """
        The property of the instance_trees.
        :rtype: dict
        """
        return self.__instance_trees

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
        if self.instance_trees.get(instance_id) is not None:
            raise DuplicateKeyException()

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

    def get_or_create_instance(self, instance_number):
        """
        Get the instance tree when it already exists, create one if it doesn't.
        :param instance_number: The instance number to be searched/created on
        :rtype: Tree
        """
        if instance_number not in self.instance_trees:
            component = ItasksComponent(
                qwidget=self.main_widget,
                qlayout=self.main_layout,
                main=True
            )
            self.add_instance_tree(instance_number, component)

        return self.get_instance_tree(instance_number)

    def handle_instruction(self, json_instruction):
        """
        Read the iTasks json and determine if you received a known or an unknown
        instance. Create or get the instance according to that.
        Call the UIGenerator with the "change"-part of the JSON and the tree.
        :param json_instruction: The instruction received from the iTasks server
        :rtype: void
        """
        try:
            parsed_json = json.loads(json_instruction)
        except ValueError:
            parsed_json = json_instruction
        except TypeError:
            parsed_json = json_instruction

        # This is dependent on the iTasks version you use.
        # TODO: remove.
        if "instanceNo" in json_instruction:
            instance = parsed_json.get("instanceNo")
        else:
            instance = parsed_json.get("instance")

        current_tree = self.get_or_create_instance(instance)

        UIGenerator.change_or_replace(
            node=current_tree.root,
            change=parsed_json.get("change")
        )

        self.main_window.show()
        self.main_widget.update()

    def close_event(self, q_close_event):  # pylint: disable-msg=C0103,W0613
        """
        Close window event, the server has to be closed as well
        :param q_close_event: The event thrown by pyqt
        :rtype: void
        """
        self.itasks_service.stop_server()

    def new_session_callback(self, instance_no, instance_key):
        """
        Callback method for the creation of a new session
        :param instance_no: iTasks instance number
        :param instance_key: iTasks instance key
        :rtype: void
        """
        self.itasks_service.attach_task_instance(
            instance_no, instance_key, self.application_callback)

    def application_callback(self, data):
        """
        Task instance callback method. This method goes to the palindrome task.
        This task has taskvalue 17, as we can see in the third if-statement.
        :param data: iTasks response data
        :rtype: void
        """

        # Start the palindrome task
        if self.temp_start_palindrome == 0:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 7, "action": "Continue"})
        if self.temp_start_palindrome == 1:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 41, "action": "New"})
        if self.temp_start_palindrome == 2:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 63, "edit": "v", "value": [17]})
        if self.temp_start_palindrome == 3:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 61, "action": "Start task"})
        if self.temp_start_palindrome == 4:
            attributes = data['change']['children'][0][2]['children']
            attributes = attributes[0][2]['children'][0][2]['children']
            attributes = attributes[1][2]['children'][0]['attributes']
            instance_no = attributes['instanceNo']
            instance_key = attributes['instanceKey']
            self.itasks_service.attach_task_instance(
                instance_no, instance_key, self.task_callback)

        self.temp_start_palindrome += 1

    def handle_callback_instructions(self):
        """
        Handles all callback instructions that are in the current queue.
        :rtype: void
        """
        while True:
            try:
                data = self.callback_queue.get(False)
                self.handle_instruction(data)
            except queue.Empty:  # raised when queue is empty
                break

    def task_callback(self, data):
        """
        Fills queue with instructions for handling an itasks task.
        :param data: iTasks task as an instruction
        :rtype: void
        """
        self.callback_queue.put(data)
