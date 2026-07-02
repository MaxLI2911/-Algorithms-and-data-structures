import matplotlib.pyplot as plt
import gc
from time import process_time
from random import randint
from Trees import BinarySearchTree, AVLTree
from typing import Callable

size_to_test = range(1000, 10001, 1000)
numbers = [randint(1, 30000) for _ in range(10000)]

create_bst_times = []
create_avl_times = []

search_bst_times = []
search_avl_times = []

remove_bst_times = []

def draw_plots():
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(size_to_test, create_bst_times, label="Drzewo BST")
    ax.plot(size_to_test, create_avl_times, label="Drzewo AVL")
    ax.legend()
    ax.set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Tworzenie drzewa",
    )
    ax.grid()
    fig.savefig("creating_trees.png")

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(size_to_test, search_bst_times, label="Drzewo BST")
    ax.plot(size_to_test, search_avl_times, label="Drzewo AVL")
    ax.legend()
    ax.set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Wyszukiwanie n pierwszych liczb w drzewie",
    )
    ax.grid()
    fig.savefig("searching_trees.png")

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.plot(size_to_test, remove_bst_times)
    ax.set(
        xlabel="Liczba elementów",
        ylabel="Czas (s)",
        title="Usuwanie n pierwszych liczb w drzewie",
    )
    ax.grid()
    fig.savefig("removing_bst.png")


def measure_time(func: Callable, size: int, array: list):
    start_time = process_time()
    for number in numbers[:size]:
        func(number)
    stop_time = process_time()
    gc.collect()
    array.append(stop_time - start_time)


if __name__ == "__main__":
    gc_old = gc.isenabled()
    gc.disable()
    for size in size_to_test:
        print("Size inserting:", size)
        bst = BinarySearchTree()
        avl = AVLTree()

        measure_time(bst.addNode, size, create_bst_times)
        measure_time(avl.addNode, size, create_avl_times)

    for size in size_to_test:
        print("Size searching:", size)

        measure_time(bst.findNode, size, search_bst_times)
        measure_time(avl.findNode, size, search_avl_times)
    
    for size in size_to_test:
        print("Size removing:", size)
        tree = bst

        measure_time(tree.removeNode, size, remove_bst_times)
    if gc_old:
        gc.enable()
    draw_plots()
