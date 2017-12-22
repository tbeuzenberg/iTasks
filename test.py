from tree_components import (
    Node,
    Tree
)


tree = Tree("root")

tree.insert("fc", [3])
tree.insert("sc", [3, 8])
tree.insert("tc", [3, 5])

tree.print()


