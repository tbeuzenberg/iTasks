import json
import sys

from PyQt5.QtWidgets import QApplication

from ui_generator import components
from tree_components import (
    Tree,
    Node
)


class UIGenerator:
    """ Generator of UI elements """
    applications = {}

    def add_application(self, itasks_id, application):
        self.applications[itasks_id] = Tree(root_node=Node(application))

    def get_application(self, itasks_id):
        return self.applications[itasks_id].root.value

    def get_tree(self, itasks_id):
        return self.applications[itasks_id]

    def add_component_to_application(self, itasks_id, location,
                                     json_component=""):
        current_application: Tree = self.applications[itasks_id]

        component_data = json.loads(json_component)
        create_component_action = getattr(
            components.Components,
            component_data["type"].lower()
        )

        parent = current_application.find_node(index_list=location).value

        component = create_component_action(
            iconCls=component_data["attributes"],
            parent=parent
        )

        # TODO: If one of these two fails, both have to throw an error
        # TODO: (and no component has to be created)

        current_application.insert(node=Node(component), index_list=location)


if __name__ == '__main__':
    generator = UIGenerator()

    generator.add_application(itasks_id="1", application=QApplication(sys.argv))

    generator.add_component_to_application(
        itasks_id=1,
        location=[],
        json_component='{"type": "Icon","attributes": {"hint": "Please enter a single line of text (this value is required)","hint-type": "info","iconCls": "icon-info","marginLeft": 5,"tooltip": "Please enter a single line of text (this value is required)"}}'
    )

    sys.exit(generator.get_application(itasks_id="1").exec_())
