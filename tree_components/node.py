""" Node component file """


class Node:
    """ Node component to store data in. This is also a subtree. """

    def __init__(self, value=None, valid=True):
        """
        Setting the parameters of the instance, node has children, these
        should be nodes.
        Nodes can be invalid. This means that the node is just created for
        another, valid node on a higher index.
        :param value: Value which the node has to hold
        :param valid: Boolean that tells if the node is valid whether or not
        :rtype: void
        """
        self.value = value
        self.__children = []
        self.__valid = valid

    @property
    def children(self):
        """ Children property """
        return self.__children

    @children.setter
    def children(self, children):
        self.__children = children

    @property
    def valid(self):
        """ Valid property """
        return self.__valid and self.value is not None

    def __add_child(self, node, index):
        """
        Add child to the current node.
        :param node: Node which has to be added
        :param index: The index on which the node has to be added
        :rtype: void
        """
        if index >= len(self.__children):
            for _ in range(len(self.__children), index):
                self.__children.append(Node(valid=False))
        self.__children.append(node)

    def __replace_child(self, node, index):
        """
        Replace the existing child with the node given through the parameters
        :param node: The new node
        :param index: The index on which we have to replace the node
        :rtype: void
        """
        self.__children[index] = node

    def add_or_replace_child(self, node, index):
        """
        Chooses whether a node has to be added or replaced, and acts accordingly
        :param node: Node that has to be added
        :param index: The index passed through the add_child or replace_child
        method
        :rtype: void
        """
        if index >= len(self.__children):
            self.__add_child(node=node, index=index)
        else:
            self.__replace_child(node=node, index=index)

    def get_child(self, index):
        """
        Get a child of the current node specified by the index
        :param index: The index we have to find the child on
        :rtype: void
        """
        return self.__children[index]

    def find_node(self, index_list):
        """
        Recursively search a node through my current children.
        When the list only has one element, we have to get that child.
        When the list has multiple elements, it means we have to search through
        the children.
        :param index_list: List of the indexes we have to search on
        :rtype: Node
        """
        if len(index_list) == 1:
            if self.get_child(index=index_list[0]).valid:
                return self.get_child(index=index_list[0])
            else:
                raise IndexError()
        else:
            first_element = index_list[:1]
            rest = index_list[1:]
            return self.__children[first_element[0]].find_node(index_list=rest)

    def print(self, prefix=""):
        """
        Recursively print the tree of the current node.
        Print the value and the nodes children after that.
        :param prefix: Helper to know what indentation the printer needs
        :type: void
        """
        if self.valid:
            print(prefix + type(self.value).__name__)
        else:
            print(prefix + "None")

        if self.__children:
            for i in range(0, len(self.__children)):
                self.__children[i].print(prefix + "- ")

    def reset(self):
        self.value.reset(self.__children)
        self.__children = []
        self.__valid = False
