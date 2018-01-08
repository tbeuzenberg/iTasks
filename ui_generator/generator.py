import json
import sys

from temporary_dir.json_components import *

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton
)
from itasks_components import ItasksComponent
from ui_generator import components
from tree_components import (
    Tree,
    Node,
)


class UIGenerator:
    """ Generator of UI elements """
    frame_widgets = {}

    def __init__(self, application):
        self.__application = application

    @property
    def application(self):
        return self.__application

    def add_widget(self, itasks_id, widget):
        self.frame_widgets[itasks_id] = Tree(root_node=Node(ItasksComponent(qwidget=widget)))

    def get_widget(self, itasks_id):
        return self.frame_widgets[itasks_id].root.value

    def get_tree(self, itasks_id):
        return self.frame_widgets[itasks_id]

    def get_component_from_widget(self, itasks_id, location):
        return self.frame_widgets[itasks_id].find_node(index_list=location)

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

        parent = current_widget.find_node(index_list=location).value.qwidget

        # TODO: If one of these two fails, both have to throw an error
        # TODO: (and no component has to be created)
        component = create_component_action(
            parent=parent,
            **component_data["attributes"],
        )

        if not location:
            location = [0]
        current_widget.insert(node=Node(ItasksComponent(qwidget=component)), index_list=location)


if __name__ == '__main__':
    generator = UIGenerator(QApplication(sys.argv))

    generator.add_widget(itasks_id=1, widget=QMainWindow())

    generator.add_component_to_widget(
        itasks_id=1,
        location=[],
        json_component=get_button()
    )

    ding = generator.get_component_from_widget(itasks_id=1, location=[0])

    print(ding.value)


    generator.get_widget(1).qwidget.show()
    sys.exit(generator.application.exec_())



