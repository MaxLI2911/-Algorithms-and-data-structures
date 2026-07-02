import pytest
from Trees import BinarySearchTree, AVLTree


@pytest.fixture
def bst():
    tree = BinarySearchTree()
    for value in [8, 3, 10, 1, 6, 14, 6]:
        tree.addNode(value)
    return tree


@pytest.fixture
def avl():
    tree = AVLTree()
    for value in [10, 20, 30, 40, 50]:
        tree.addNode(value)
    return tree

def test_add_and_find_node(bst: BinarySearchTree):
    assert bst.findNode(8) is not None
    assert bst.findNode(6) is not None
    assert bst.findNode(6).quantity == 2
    assert bst.findNode(99) is None


def test_remove_node_quantity(bst: BinarySearchTree):
    bst.removeNode(6)
    node = bst.findNode(6)
    assert node is not None
    assert node.quantity == 1


def test_remove_node_completely(bst: BinarySearchTree):
    bst.removeNode(6)
    bst.removeNode(6)
    assert bst.findNode(6) is None


def test_remove_leaf(bst: BinarySearchTree):
    bst.removeNode(1)
    assert bst.findNode(1) is None


def test_remove_node_with_children(bst: BinarySearchTree):
    bst.removeNode(3)
    assert bst.findNode(3) is None


def test_avl_balance_property(avl: AVLTree):
    def is_balanced(node):
        if node is None:
            return True
        balance = avl.getBalance(node)
        return -1 <= balance <= 1 and is_balanced(node.left_child) and is_balanced(node.right_child)
    assert is_balanced(avl.root)


def test_avl_left_rotation():
    tree = AVLTree()
    tree.addNode(1)
    tree.addNode(2)
    tree.addNode(3)
    assert tree.root.value == 2


def test_avl_right_rotation():
    tree = AVLTree()
    tree.addNode(3)
    tree.addNode(2)
    tree.addNode(1)
    assert tree.root.value == 2
