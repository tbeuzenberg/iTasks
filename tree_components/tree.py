# TODO: Add items when insert on unknown index


class Tree:
    def __init__(self, root_node):
        """
        Set the properties of the Tree class.
        :param root_node: The root node of the current tree
        :rtype: void
        """
        self.root = root_node

    def search_node(self, index_list):
        """
        Call the search_node of the root node
        :param index_list: The index_list the Node.search_node uses to search
        :rtype: void
        """
        return self.root.search_node(index_list=index_list)

    def insert(self, node, index_list):
        """
        Insert the node on a specific place in the tree.
        Firstly, search a node by the first items of the string (except if
        there is only one item in the list)
        Then, call add_or_replace_child to add the item to the found node.
        :param node: Node you want to insert
        :param index_list: Indexes you want to place the node on
        :rtype: void
        """
        if len(index_list) <= 1:
            self.root.add_or_replace_child(node=node, index=index_list[0])
        else:
            last = index_list[len(index_list) - 1:]
            rest = index_list[:len(index_list) - 1]

            self.root.search_node(index_list=rest).add_or_replace_child(
                node=node,
                index=last[0]
            )

    def print(self):
        """
        Print the tree of the root node
        :rtype: void
        """
        self.root.print()
