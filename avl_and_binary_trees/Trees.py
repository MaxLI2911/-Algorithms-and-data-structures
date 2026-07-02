class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.quantity = 1
        self.height = 1


class BinarySearchTree:
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            for value in values:
                self.addNode(value)

    def addNode(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        return self._addNode(self.root, val)

    def _addNode(self, currentNode, val):
        if val < currentNode.value:
            if currentNode.left_child is None:
                currentNode.left_child = Node(val)
            else:
                self._addNode(currentNode.left_child, val)
        elif val > currentNode.value:
            if currentNode.right_child is None:
                currentNode.right_child = Node(val)
            else:
                self._addNode(currentNode.right_child, val)
        else:
            currentNode.quantity += 1

    def findNode(self, val):
        if self.root is None:
            return None
        return self._findNode(self.root, val)

    def _findNode(self, currentNode, val):
        if val == currentNode.value:
            return currentNode
        elif val < currentNode.value and currentNode.left_child is not None:
            return self._findNode(currentNode.left_child, val)
        elif val > currentNode.value and currentNode.right_child is not None:
            return self._findNode(currentNode.right_child, val)
        else:
            return None

    def removeNode(self, val):
        self.root = self._removeNode(self.root, val)

    def _removeNode(self, currentNode, val):
        if currentNode is None:
            return None

        if val < currentNode.value:
            currentNode.left_child = self._removeNode(currentNode.left_child, val)
        elif val > currentNode.value:
            currentNode.right_child = self._removeNode(currentNode.right_child, val)
        else:
            if currentNode.quantity > 1:
                currentNode.quantity -= 1
                return currentNode

            if currentNode.left_child is None:
                return currentNode.right_child
            elif currentNode.right_child is None:
                return currentNode.left_child

            min_larger_node = self._findMin(currentNode.right_child)
            currentNode.value = min_larger_node.value
            currentNode.quantity = min_larger_node.quantity
            min_larger_node.quantity = 1
            currentNode.right_child = self._removeNode(currentNode.right_child, min_larger_node.value)
        return currentNode

    def _findMin(self, node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def printTree(self, node=None, indent="", is_left=True):
        if node is None:
            node = self.root
        if node.right_child:
            new_indent = indent + ("│   " if is_left else "    ")
            self.printTree(node.right_child, new_indent, False)

        node_str = f"{node.value}" + (f"({node.quantity})" if node.quantity > 1 else "")
        print(indent + ("└── " if is_left else "┌── ") + node_str)

        if node.left_child:
            new_indent = indent + ("    " if is_left else "│   ")
            self.printTree(node.left_child, new_indent, True)


class AVLTree(BinarySearchTree):
    def addNode(self, val):
        self.root = self._addNode(self.root, val)

    def _addNode(self, node, val):
        if not node:
            return Node(val)
        elif val < node.value:
            node.left_child = self._addNode(node.left_child, val)
        elif val > node.value:
            node.right_child = self._addNode(node.right_child, val)
        else:
            node.quantity += 1
            return node

        self.updateHeight(node)
        return self.rebalance(node)

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def updateHeight(self, node):
        node.height = max(self.getHeight(node.left_child), self.getHeight(node.right_child)) + 1

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left_child) - self.getHeight(node.right_child)

    def leftRotate(self, z):
        y = z.right_child
        t = y.left_child

        y.left_child = z
        z.right_child = t

        self.updateHeight(z)
        self.updateHeight(y)

        return y

    def rightRotate(self, z):
        y = z.left_child
        t = y.right_child

        y.right_child = z
        z.left_child = t

        self.updateHeight(z)
        self.updateHeight(y)

        return y

    def rebalance(self, node):
        balance = self.getBalance(node)

        if balance > 1:
            if self.getBalance(node.left_child) < 0:
                node.left_child = self.leftRotate(node.left_child)
            return self.rightRotate(node)

        if balance < -1:
            if self.getBalance(node.right_child) > 0:
                node.right_child = self.rightRotate(node.right_child)
            return self.leftRotate(node)

        return node


