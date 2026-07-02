# Binary Search Tree (BST) vs. AVL Tree Performance Analysis

## Performance Results Summary

### 1. Tree Creation 
![image](avl_and_binary_trees/creating_trees.png)
* **Observations:** Building an AVL tree takes significantly more time compared to a standard BST. At 10,000 elements, AVL tree construction requires approximately `0.056` seconds, whereas the BST requires around `0.011` seconds.
* **Analysis:** The overhead in AVL tree creation stems from the strict balancing property. Every insertion requires checking the balance factor and performing necessary single or double rotations ($O(\log n)$ per insertion), whereas the BST performs straightforward insertions without rebalancing.

### 2. Searching Elements 
![image](avl_and_binary_trees/searching_trees.png)
* **Observations:** The AVL tree consistently outperforms the BST during lookup operations, especially as the number of elements scales. For 10,000 elements, searching in the BST takes roughly `0.012` seconds, while the AVL tree finishes in less than `0.010` seconds.
* **Analysis:** Because the AVL tree guarantees a strictly balanced height of $O(\log n)$, the maximum search path is minimized. In contrast, the standard BST can become partially unbalanced depending on the insertion order, leading to deeper branches and longer search times.

### 3. Deletion in BST 
![image](avl_and_binary_trees/removing_bst.png)
* **Observations:** The benchmark shows the time taken to remove the first $n$ numbers from a BST. The deletion time scales linearly up to about 7,000 elements (reaching `0.008` seconds) and then exhibits a slight stabilization/decrease towards 10,000 elements.
* **Analysis:** Deletion complexity is directly related to node depth and tree restructuring (finding successors/predecessors). The curve reflects the changing shape of the BST as elements are progressively removed.

## Conclusion
* **BST** is faster for scenarios dominated by frequent insertions where subsequent lookup performance is not critical.
* **AVL Tree** is ideal for lookups/search-heavy applications where the upfront cost of balancing during insertion is justified by guaranteed, optimal $O(\log n)$ search times.
