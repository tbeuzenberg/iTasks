""" File for the UI-generator """
import json

from tree_components import Node
from ui_generator import components


class UIGenerator:
    """ Generator of UI elements """

    @staticmethod
    def change_or_replace(node, change):
        """
        Choose whether the change instruction describes a replace or a change
        command
        :param change: The changes that have to be read
        :param current_node: The current node the changes have to apply on
        :rtype: void
        """

        if change["type"] == "replace":
            UIGenerator.read_replace_ui_instruction(
                parent_node=node,
                index=0,
                replace_instruction=change["definition"]
            )

        if change["type"] == "change":
            UIGenerator.read_change_ui_instruction(
                current_node=node,
                change_instruction=change
            )

    @staticmethod
    def read_replace_ui_instruction(parent_node, index, replace_instruction):
        """
        Read the replace instruction recursively and calls factory methods.
        :param parent_node: The parent node to replace the children from
        :param index: the index on the parent node of the components that has
        to be replaced
        :param replace_instruction: The data containing a name, attributes and
        children.
        :rtype: void
        """
        created_component = UIGenerator.create_component(
            type=replace_instruction["type"],
            parent_node=parent_node,
            index=index,
            attributes=replace_instruction.get("attributes")
        )

        created_node = Node(created_component)

        parent_node.add_or_replace_child(
            index=index,
            node=created_node
        )

        children = replace_instruction.get("children")
        if children:
            for key, child in enumerate(children):
                UIGenerator.read_replace_ui_instruction(
                    parent_node=created_node,
                    index=key,
                    replace_instruction=child
                )

    @staticmethod
    def create_component(type, parent_node, index, attributes):
        """
        Calling the create component factory to create a component. Also checks
        if the component is known in the application.
        :param type: The type of the to be created component
        :param parent_node: The node on which the component has to be created on
        :param index: The index the component has to be created on
        :param attributes: The attributes of the to be created component
        :rtype: ItasksComponent
        """
        if type.lower() in dir(components.Components):
            create_component_action = getattr(
                components.Components,
                type.lower()
            )
        else:
            create_component_action = components.Components.unknown_component

        # if "direction" in attributes:
        #     attributes.pop("direction")

        return create_component_action(
            parent=parent_node.value,
            index=index,
            **attributes
        )

    @staticmethod
    def read_change_ui_instruction(current_node, change_instruction):
        """

        :param current_node: The current node of which elements have to be
        replaced
        :param change_instruction:
        :rtype: void
        """
        children = change_instruction.get("children")
        attributes = change_instruction.get("attributes")

        if len(attributes) > 0:
            attributes = attributes[0]

        for child in children:
            if child[1] == "change":
                UIGenerator.change_or_replace(
                    node=current_node.get_child(child[0]),
                    change=child[2],
                )
            else:
                raise NotImplementedError

    # # TODO: This function is too long, should be cut into different parts
    # def add_component_to_widget(self, instance_id, location,
    #                             json_component=""):
    #     # TODO: Location has to be relative to the previously added component
    #     # TODO: No idea how we should fix this yet.
    #     current_widget = self.instance_trees[instance_id]
    #
    #     component_data = json.loads(json_component)
    #
    #     # dir() might actually take pretty long, I have no idea.
    #     if component_data["type"].lower() in dir(components.Components):
    #         create_component_action = getattr(
    #             components.Components,
    #             component_data["type"].lower()
    #         )
    #     else:
    #         create_component_action = components.Components.unknown_component
    #
    #     parent_location = location[:len(location) - 1]
    #
    #     parent = current_widget.find_node(index_list=parent_location).value
    #
    #     # TODO: If one of these two fails, both have to throw an error
    #     # TODO: (and no component has to be created)
    #     component = create_component_action(
    #         parent=parent,
    #         **component_data["attributes"],
    #     )
    #
    #     if not location:
    #         location = [0]
    #     current_widget.insert(node=Node(component), index_list=location)