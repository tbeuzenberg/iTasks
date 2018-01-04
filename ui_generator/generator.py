import json
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)

from ui_generator import components
from tree_components import (
    Tree,
    Node
)


class UIGenerator:
    """ Generator of UI elements """
    frame_widgets = {}

    def __init__(self, application):
        self.__application = application

    def get_application(self):
        return self.__application

    def add_widget(self, itasks_id, widget):
        self.frame_widgets[itasks_id] = Tree(root_node=Node(widget))

    def get_widget(self, itasks_id):
        return self.frame_widgets[itasks_id].root.value

    def get_tree(self, itasks_id):
        return self.frame_widgets[itasks_id]

    def get_component_from_widget(self, itasks_id, location):
        return self.frame_widgets[itasks_id].find_node(index_list=location)

    def add_component_to_widget(self, itasks_id, location,
                                json_component=""):
        current_widget: Tree = self.frame_widgets[itasks_id]

        component_data = json.loads(json_component)
        create_component_action = getattr(
            components.Components,
            component_data["type"].lower()
        )

        parent = current_widget.find_node(index_list=location).value

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

    generator.add_widget(itasks_id=1, widget=QWidget())

    generator.add_component_to_widget(
        itasks_id=1,
        location=[],
        json_component='{"type": "Icon","attributes": {"hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'
    )

    generator.add_component_to_widget(
        itasks_id=1,
        location=[],
        json_component='{"type": "Label","attributes": {"value": "Ik ben Pieter haha", "hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'
    )

    generator.add_component_to_widget(
        itasks_id=1,
        location=[],
        json_component='{"type": "button","attributes": {"value": "Ik ben Pieter haha", "hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'
    )

    generator.get_widget(1).show()
    sys.exit(generator.get_application().exec_())



