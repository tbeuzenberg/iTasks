class Node:
    def __init__(self, value=None):
        """
        Setting the parameters of the instance, node has children, these
        should be nodes.
        :param value: Value which the node has to hold
        :rtype: void
        """
        self.value = value
        self.children = []

    def add_child(self, node, index):
        """
        Add child to the current node.
        :param node: Node which has to be added
        :param index: The index on which the node has to be added
        :rtype: void
        """
        if index >= len(self.children):
            for i in range(0, index):
                    self.children.append(Node())
        self.children.append(node)

    def replace_child(self, node, index):
        """
        Replace the existing child with the node given through the parameters
        :param node: The new node
        :param index: The index on which we have to replace the node
        :rtype: void
        """
        self.children[index] = node

    def add_or_replace_child(self, node, index):
        """
        Chooses whether a node has to be added or replaced, and acts accordingly
        :param node: Node
        :param index: int
        :rtype: void
        """
        if index >= len(self.children):
            self.add_child(node=node, index=index)
        else:
            self.replace_child(node=node, index=index)

    def get_child(self, index):
        """
        Get a child of the current node specified by the index
        :param index: The index we have to find the child on
        :rtype: void
        """
        return self.children[index]

    def search_node(self, index_list):
        """
        Recursively search a node through my current children.
        When the list only has one element, we have to get that child.
        When the list has multiple elements, it means we have to search through
        the children.
        :param index_list: List of the indexes we have to search on
        :return:
        """
        if len(index_list) == 1:
            return self.get_child(index=index_list[0])
        else:
            first_element = index_list[:1]
            rest = index_list[1:]
            return self.children[first_element[0]].search_node(index_list=rest)

    def print(self, prefix=""):
        """
        Recursively print the tree of the current node.
        Print the value and the nodes children after that.
        :param prefix: Helper to know what indentation the printer needs
        :return:
        """
        if self.value is None:
            print(prefix + "None")
        else:
            print(prefix + type(self.value).__name__)

        if len(self.children) > 0:
            for i in range(0, len(self.children)):
                self.children[i].print(prefix + "- ")
