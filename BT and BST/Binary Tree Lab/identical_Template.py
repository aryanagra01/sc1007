# ============================================================================
# Lab 3 Q4 (Navigator) – identical(tree1, tree2)
# ============================================================================
# DESCRIPTION
# Write a recursive Python function identical() to determine whether two
# binary trees are structurally identical, assuming the two binary trees as
# tree1 and tree2. This function returns TRUE if two binary trees are
# structurally identical; otherwise, it returns FALSE.
#
# Two binary trees are structurally identical if they are both empty, or if
# they are both non-empty and the left and right subtrees are similar
# (same values, arranged the same way).
#
# TASK
# Complete identical(tree1, tree2) and return True or False.
#
# From the answer key:
#   - both None            -> True
#   - only one is None     -> False
#   - values are different -> False
#   - else recurse on both lefts AND both rights
# ============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, items):
        """Build a binary tree from a level-order list (None = missing node)."""
        if not items:
            return None

        nodes = [cls(val) if val is not None else None for val in items]
        for i, node in enumerate(nodes):
            if node is None:
                continue
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            if left_idx < len(nodes):
                node.left = nodes[left_idx]
            if right_idx < len(nodes):
                node.right = nodes[right_idx]
        return nodes[0]


class Solution:
    def identical(self, tree1, tree2):
        # -------- DO NOT MODIFY ANYTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------
        # Write your code below #

        # both empty
        if tree1 is None and tree2 is None:
            return True

        # only one is empty
        if tree1 is None or tree2 is None:
            return False

        # values are different
        if tree1.val != tree2.val:
            return False

        # same value here — both lefts AND both rights must also match
        return self.identical(tree1.left, tree2.left) and self.identical(tree1.right, tree2.right)
        # -------- DO NOT MODIFY ANYTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------


def run_test():
    test_cases = [
        # same tree
        ({"tree1": [3, 5, 1, 2, 4, 6], "tree2": [3, 5, 1, 2, 4, 6]}, True),
        # one node each, same
        ({"tree1": [1], "tree2": [1]}, True),
        # both empty
        ({"tree1": [], "tree2": []}, True),
        # different values
        ({"tree1": [3, 5, 1], "tree2": [3, 5, 2]}, False),
        # one empty
        ({"tree1": [1], "tree2": []}, False),
    ]
    for inputs, expected in test_cases:
        tree1 = TreeNode.from_list(inputs["tree1"])
        tree2 = TreeNode.from_list(inputs["tree2"])
        result = Solution().identical(tree1, tree2)
        passed = result == expected
        print("Input:   ", inputs)
        print("Output:  ", result)
        print("Expected:", expected)
        print("Passed:  ", passed)
        print()


if __name__ == "__main__":
    run_test()
