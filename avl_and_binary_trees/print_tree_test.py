from Trees import BinarySearchTree, AVLTree


tree1 = BinarySearchTree()
for value in [8, 3, 11, 1, 6, 10, 6, 12]:
    tree1.addNode(value)

tree2 = AVLTree()
for value in [10, 20, 30, 40, 50]:
    tree2.addNode(value)

tree1.printTree()
print()
tree1.removeNode(1)
tree1.printTree()
print()
print()
print()
tree2.printTree()
print()

tree = AVLTree()
tree.addNode(1)
tree.addNode(2)
tree.printTree()
tree.addNode(3)
tree.printTree()
tree.addNode(4)
tree.printTree()
tree.addNode(5)
tree.printTree()
tree.addNode(6)
tree.printTree()
print()
tree3 = BinarySearchTree()
tree3.addNode(1)
tree3.addNode(2)
tree3.printTree()
tree3.addNode(3)
tree3.printTree()