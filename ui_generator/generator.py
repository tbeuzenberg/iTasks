import json
import sys

from temporary_dir.json_components import *

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton
)

from ui_generator import components
from tree_components import (
    Tree,
    Node
)


class UIGenerator:
    """ Generator of UI elements """
    frame_widgets = {}

    def __init__(self, application: QApplication):
        self.__application = application

    @property
    def application(self):
        return self.__application

    def add_widget(self, itasks_id, widget: QWidget):
        self.frame_widgets[itasks_id] = Tree(root_node=Node(widget))

    def get_widget(self, itasks_id):
        if itasks_id not in self.frame_widgets:
            raise IndexError()
        return self.frame_widgets[itasks_id].root.value

    def get_component_from_widget(self, itasks_id, location):
        return self.frame_widgets[itasks_id].find_node(index_list=location)

    def read_itasks_json_instruction(self, itasks_json_instruction):

        itasks_instruction = json.loads(itasks_json_instruction)

        instance_number = itasks_instruction["instance"]
        change = itasks_instruction["change"]

        if instance_number not in self.frame_widgets:
            self.add_widget(itasks_id=instance_number, widget=QWidget())

        current_widget = self.get_widget(itasks_id=instance_number)

        if change["type"] == "replace":
            self.replace_ui(
                widget=current_widget,
                replace_instruction=change["definition"]
            )

        if change["type"] == "change":
            self.change_ui(
                widget=current_widget,
                change_instruction=change
            )

    def replace_ui(self, widget, replace_instruction):
        raise NotImplementedError
    #     possible_components = dir(components.Components)
    #
    #     for item in replace_instruction:
    #         if item[replace_instruction['type']] in possible_components:
    #             self.__add_component_to_widget()

    def change_ui(self, widget, change_instruction):
        # possible_components = dir(components.Components)

        for item in change_instruction:
            print(item)


    def __add_component_to_widget(self, itasks_id, location, type,
                                  attributes=None, children=None):
        raise NotImplementedError

    # TODO: This function is too long, should be cut into different, smaller, parts
    def add_component_to_widget(self, itasks_id, location,
                                json_component=""):
        # TODO: Location has to be relative to the previously added component
        # TODO: No idea how we should fix this yet.
        current_widget: Tree = self.frame_widgets[itasks_id]

        component_data = json.loads(json_component)

        # dir() might actually take pretty long, I have no idea.
        if component_data["type"].lower() in dir(components.Components):
            create_component_action = getattr(
                components.Components,
                component_data["type"].lower()
            )
        else:
            create_component_action = components.Components.unknown_component

        parent_location = location[:len(location) - 1]

        parent = current_widget.find_node(index_list=parent_location).value

        # TODO: If one of these two fails, both have to throw an error
        # TODO: (and no component has to be created)
        component = create_component_action(
            parent=parent,
            **component_data["attributes"],
        )

        if not location:
            location = [0]
        current_widget.insert(node=Node(component), index_list=location)


if __name__ == '__main__':
    generator = UIGenerator(QApplication(sys.argv))

    generator.read_itasks_json_instruction(get_change())

    sys.exit(generator.application.exec_())

    # generator = UIGenerator(QApplication(sys.argv))
    #
    # generator.add_widget(itasks_id=1, widget=QMainWindow())
    #
    # btn3 = get_button(width=50, height=500, enabled=False)
    # btn2 = get_button(width=150, height=200)
    # btn1 = get_button(width=150, height=500)
    #
    #
    # generator.add_component_to_widget(
    #     itasks_id=1,
    #     location=[0],
    #     json_component=btn1
    # )
    #
    # generator.add_component_to_widget(
    #     itasks_id=1,
    #     location=[2],
    #     json_component=btn2
    # )
    #
    # generator.add_component_to_widget(
    #     itasks_id=1,
    #     location=[0, 2],
    #     json_component=btn3
    # )
    #
    # generator.get_widget(1).show()
    # sys.exit(generator.application.exec_())
