from tree_components import (
    Node,
    Tree
)


tree = Tree(Node())

tree.insert(Node(), [3])
tree.insert(Node(), [3, 8])
tree.insert(Node(), [3, 5])

tree.print()


