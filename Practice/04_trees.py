"""
Binary tree and BST practice. Fill each function, then run this file.

node.data, node.left, node.right.
BST insert order is given in the check. Empty tree is None.
"""

from _support import BTNode, bst_from, inorder, check


def sum_of_leaf_nodes(root):
    """Sum of nodes with no children. Use recursion.
    Insert 10, 5, 20, 3, 7, 30. Leaves 3, 7, 30. Sum 40.
    """
    if root is None:
        return 0
    if root.right or root.left:
        return sum_of_leaf_nodes(root.right) + sum_of_leaf_nodes(root.left)
    else: 
        return root.data


def sum_of_non_leaf_nodes(root):
    """Sum of nodes that have at least one child.
    Same tree. 10 + 5 + 20 = 35.
    """

    if root is None:
        return 0
    if root.right or root.left:
        return root.val + sum_of_non_leaf_nodes(root.right) + sum_of_leaf_nodes(root.left)
    else:
        return 0


def smallest_value(root):
    """Smallest value in a binary tree. This is not told it is a BST,
    so you cannot only walk left unless you are using the BST one below.
    Tree 4, left 5, right 2, and 2 has children 3 and 1. Answer 1.
    """
    raise NotImplementedError


def print_smaller_values(root, m):
    """Return every value strictly less than m. Order does not matter.
    Same tree, m = 4 -> 2, 3, 1.
    """
    raise NotImplementedError


def mirror(root):
    """Swap every left and right child. Change the tree. Return the root.
    """
    raise NotImplementedError


def identical(tree1, tree2):
    """True when both trees have the same shape and the same values.
    """
    raise NotImplementedError


def has_grandchild(root):
    """Return the values of nodes that have at least one grandchild.
    A grandchild is a child of a child.
          1
         / \
        2   3
       /
      4
    Answer [1]. 2's child 4 is not a grandchild of 2.
    """
    raise NotImplementedError


def max_depth(root):
    """Number of nodes on the longest path from root to a leaf.
    Empty tree -> 0. A single node -> 1.
    """
    raise NotImplementedError


def inorder_iterative(root):
    """In-order with one stack. No recursion. Return the list.
    BST 10, 5, 20 -> [5, 10, 20]
    """
    raise NotImplementedError


def postorder_one_stack(root):
    """Post-order with one stack. No recursion. Return the list.
    BST 10, 5, 20 -> [5, 20, 10]
    """
    raise NotImplementedError


def postorder_two_stacks(root):
    """Post-order with two stacks. Return the list.
    BST 10, 5, 20 -> [5, 20, 10]
    """
    raise NotImplementedError


def preorder_iterative(root):
    """Pre-order with one stack. Return the list.
    BST 10, 5, 20 -> [10, 5, 20]
    """
    raise NotImplementedError


def level_order(root):
    """Level order, left to right, using a queue. Return the list.
    BST 10, 5, 20, 3 -> [10, 5, 20, 3]
    """
    raise NotImplementedError


def is_bst(root):
    """True if every node is greater than everything in its left subtree
    and smaller than everything in its right subtree.
    """
    raise NotImplementedError


def kth_smallest(root, k):
    """1-indexed. k = 1 is the smallest. Return -1 if k is out of range.
    Insert 20, 8, 22, 4, 12. k = 3 -> 12.
    """
    raise NotImplementedError


def find_lca(root, p, q):
    """Lowest common ancestor in a BST. A node can be an ancestor of itself.
    Insert 6, 2, 8, 0, 4, 7, 9. p = 2, q = 8 -> 6. p = 2, q = 4 -> 2.
    """
    raise NotImplementedError


def remove_bst(root, value):
    """Delete value from the BST. Return the new root.
    Insert 20, 8, 22, 4, 12, then delete 8.
    In-order becomes [4, 12, 20, 22].
    """
    raise NotImplementedError


def sum_greater_tree(root):
    """Each node becomes the sum of all values greater than or equal to it.
    Walk the larger nodes first.
    Insert 4, 1, 6. After the change, in-order is [11, 10, 6].
    """
    raise NotImplementedError


def _hand_tree():
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)
    return root


def _grandchild_tree():
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    return root


def _invalid_bst():
    root = BTNode(5)
    root.left = BTNode(6)
    root.right = BTNode(7)
    return root


def _different_tree():
    root = BTNode(2)
    root.left = BTNode(3)
    root.right = BTNode(1)
    return root


if __name__ == "__main__":
    leaves = [10, 5, 20, 3, 7, 30]
    check("sum leaves", lambda: sum_of_leaf_nodes(bst_from(leaves)), 40)
    check("sum non-leaves", lambda: sum_of_non_leaf_nodes(bst_from(leaves)), 35)
    check("smallest", lambda: smallest_value(_hand_tree()), 1)
    check("smaller than 4", lambda: sorted(print_smaller_values(_hand_tree(), 4)), [1, 2, 3])
    check("mirror", lambda: inorder(mirror(_hand_tree())), [1, 2, 3, 4, 6, 5])
    check("identical yes", lambda: identical(bst_from([2, 1, 3]), bst_from([2, 1, 3])), True)
    check("identical no", lambda: identical(bst_from([2, 1, 3]), _different_tree()), False)
    check("grandchild", lambda: has_grandchild(_grandchild_tree()), [1])
    check("depth", lambda: max_depth(_grandchild_tree()), 3)
    check("empty depth", lambda: max_depth(None), 0)
    check("inorder stack", lambda: inorder_iterative(bst_from([10, 5, 20])), [5, 10, 20])
    check("postorder one stack", lambda: postorder_one_stack(bst_from([10, 5, 20])), [5, 20, 10])
    check("postorder two stacks", lambda: postorder_two_stacks(bst_from([10, 5, 20])), [5, 20, 10])
    check("preorder stack", lambda: preorder_iterative(bst_from([10, 5, 20])), [10, 5, 20])
    check("level order", lambda: level_order(bst_from([10, 5, 20, 3])), [10, 5, 20, 3])
    check("is bst yes", lambda: is_bst(bst_from([6, 2, 8, 0, 4])), True)
    check("is bst no", lambda: is_bst(_invalid_bst()), False)
    check("kth", lambda: kth_smallest(bst_from([20, 8, 22, 4, 12]), 3), 12)
    check("kth out of range", lambda: kth_smallest(bst_from([20, 8]), 5), -1)
    check("lca different sides", lambda: find_lca(bst_from([6, 2, 8, 0, 4, 7, 9]), 2, 8), 6)
    check("lca is the node", lambda: find_lca(bst_from([6, 2, 8, 0, 4, 7, 9]), 2, 4), 2)
    check("remove bst", lambda: inorder(remove_bst(bst_from([20, 8, 22, 4, 12]), 8)), [4, 12, 20, 22])
    check("sum greater", lambda: inorder(sum_greater_tree(bst_from([4, 1, 6]))), [11, 10, 6])
