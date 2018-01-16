""" File for the UI-generator """
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
        :param node: The current node the changes have to apply on
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
            component_type=replace_instruction["type"],
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
    def create_component(component_type, parent_node, index, attributes):
        """
        Calling the create component factory to create a component. Also checks
        if the component is known in the application.
        :param component_type: The type of the to be created component
        :param parent_node: The node on which the component has to be created on
        :param index: The index the component has to be created on
        :param attributes: The attributes of the to be created component
        :rtype: ItasksComponent
        """
        if component_type.lower() in dir(components.Components):
            create_component_action = getattr(
                components.Components,
                component_type.lower()
            )
        else:
            create_component_action = components.Components.unknown_component

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

        current_node.update(attributes)

        for child in children:
            if child[1] == "change":
                UIGenerator.change_or_replace(
                    node=current_node.get_child(child[0]),
                    change=child[2],
                )
            else:
                raise NotImplementedError
