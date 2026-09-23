# ============================================================================
# Post-Order Traversal of Binary Tree  (postOrderIterativeS1)
# ============================================================================
# DESCRIPTION
# Write an iterative Python function postOrderIterativeS1() that returns a
# list of the node values in post-order traversal order for a binary search
# tree using only one temporary stack inside the postOrderIterativeS1()
# function. Note that you should only use push() or pop() operations when
# you add or remove integers from the stack.
#
# TASK
# Complete postOrderIterativeS1(node) and return a list of all node values
# in post-order traversal order.  (left, right, root)
#
# STACK NOTE
# There is NO Stack class given here (unlike the tutorial). You still need
# one stack, but you make it yourself with a Python list:
#   stack.append(x)  =  push
#   stack.pop()      =  pop
# Only ONE stack. Do not use recursion.
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
    def postOrderIterativeS1(self, root):
        # Write your code below #

        result = []

        if root is None:
            return result

        s = []
        s.append(root)

        while s:
            current = s.pop()
            result.append(current.val)
            if current.left:
                s.append(current.left)
            if current.right:
                s.append(current.right)

        result.reverse()
        return result


class Solution02:
    def postOrderIterativeS1(self, root):
        # Write your code below #
        result = []

        if root is None:
            return result

        stack = []
        current = root

        # Two kinds of unfinished work, so loop while either exists:
        #   current -> a subtree we haven't explored yet (need to go left)
        #   stack   -> nodes we saw but can't record yet (post-order = record LAST)
        while current or stack:

            # GO LEFT: post-order does left first, so dive to the leftmost node.
            # We pass nodes on the way down but can't record them yet
            # (their left and right come first), so save them on the stack.
            # Push right child BEFORE the node so it sits underneath as a
            # "reminder". Later, if we still see it under the parent, we know
            # the right side hasn't been done. That's how one stack replaces
            # a "visited" flag.
            while current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            # current is None here: no more left to go, so time to deal with the stack

            # Pop the latest saved node. Its left side is done (we just came
            # back from it), but we still need to check its right side.
            current = stack.pop()

            # Reminder still on top -> right subtree NOT done, so we can't
            # record current yet (post-order needs right before root).
            #   pop the reminder: we're about to handle that right child now
            #   push current back: it must wait until its right side finishes
            #   go right: treat the right subtree like a new tree (GO LEFT again)
            if current.right and stack and stack[-1] and current.right == stack[-1]:
                stack.pop()
                stack.append(current)
                current = current.right

            # No right child, or the reminder is gone. The reminder only
            # disappears once we've gone right, so the right side is done.
            # Left done + right done -> safe to record the root now.
            else:
                result.append(current.val)
                # This node is finished, so don't go left from it again
                # (that would redo its subtree). None forces the next loop
                # to skip GO LEFT and pop the parent waiting on the stack.
                current = None

        return result


# ============================================================================
# HOW YOUR SOLUTION IS TESTED  (read-only)
# ============================================================================
# For every test case in the "Test Cases" panel the grader does three things:
#   1. builds the inputs from the test-case JSON,
#   2. calls your method on a fresh Solution() object,
#   3. compares the value you return with the expected output.
#
# run_test() below shows exactly that for the first sample test cases, so you
# can see how your function is called. You do not need to call it: when you
# click Submit, the grader runs all the test cases for you in the same way.

def run_test():
    test_cases = [
        # (inputs, expected output) - the first cases from the Test Cases panel
        ({"root": []}, []),
        ({"root": [5]}, [5]),
        # extra local cases:     5
        #                       / \
        #                      3   8
        #                     / \
        #                    1   4
        ({"root": [5, 3, 8, 1, 4]}, [1, 4, 3, 8, 5]),
        ({"root": [20, 15, 50, 10, 18, 25, 80]}, [10, 18, 15, 25, 80, 50, 20]),
    ]
    for inputs, expected in test_cases:
        root = TreeNode.from_list(inputs["root"])   # level-order list -> tree
        result = Solution().postOrderIterativeS1(root)
        output = result
        passed = _same(output, expected)
        print("Input:   ", inputs)
        print("Output:  ", output)
        print("Expected:", expected)
        print("Passed:  ", passed)
        print()

def _same(a, b, ordered=True):
    """Compare like the grader: a tuple counts as a list, 2 == 2.0, and when
    ordered=False the elements of a list may appear in any order."""
    if isinstance(a, tuple): a = list(a)
    if isinstance(b, tuple): b = list(b)
    if isinstance(a, list) and isinstance(b, list):
        if not ordered:
            a, b = sorted(a, key=repr), sorted(b, key=repr)
        return len(a) == len(b) and all(_same(x, y, ordered) for x, y in zip(a, b))
    return a == b

if __name__ == "__main__":
    run_test()
