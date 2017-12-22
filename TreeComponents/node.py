class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def add_child(self, node, index):
        if index >= len(self.children):
            for i in range(0, index):
                    self.children.append(Node())
        self.children.append(node)

    def replace_child(self, node, index):
        """
        Replace the existing child with the node given through the parameters
        :param node:
        :param index:
        :return:
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
        return self.children[index]

    def search_node(self, index_list):
        if len(index_list) == 1:
            return self.get_child(index=index_list[0])
        else:
            first_element = index_list[:1]
            rest = index_list[1:]
            return self.children[first_element[0]].search_node(index_list=rest)

    def print(self, prefix=""):
        if self.value is None:
            print(prefix + "None")
        else:
            print(prefix + type(self.value).__name__)

        if len(self.children) > 0:
            for i in range(0, len(self.children)):
                self.children[i].print(prefix + "- ")
