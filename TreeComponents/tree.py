from TreeComponents.node import Node


class Tree:
    def __init__(self, root):
        self.root = root

    def search_node(self, index_list):
        return self.root.search_node(index_list=index_list)

    def insert(self, value, index_list):
        node = Node(value)

        if len(index_list) <= 1:
            self.root.add_or_replace_child(node=node, index=index_list[0])
        else:
            last = index_list[len(index_list) - 1:]
            rest = index_list[:len(index_list) - 1]

            self.root.search_node(index_list=rest).add_or_replace_child(node=node, index=last[0])

    def print(self):
        self.root.print()
