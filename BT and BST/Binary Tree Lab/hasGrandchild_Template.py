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
    def has_grandchild(self, root):

        # Write your code here #
        if root is None:
            return []

        if (root.left and (root.left.left or root.left.right) or
            root.right and (root.right.left or root.right.right)):

            return [root.val] + self.has_grandchild(root.left) + self.has_grandchild(root.right)
        else:
            return self.has_grandchild(root.left) + self.has_grandchild(root.right)

    # Lecture answer (iterative, stack-based) — same logic, different style
    # no recursion — the stack is doing what the call stack would normally do
    def has_grandchild_iterative(self, root):
        if root is None:
            return []

        result = []
        stack = [root]   # start at the top, visit everyone later

        # keep going while there are still nodes we haven't checked
        while stack:
            curr = stack.pop()
            has = False   # assume no grandchild until we actually see one

            # From the node you're on:
            #   grandchild = "does my child itself have a child?"
            # also push the child so we can check THAT node later (like recurse)

            if curr.left:
                # left child has its own left/right → curr has a grandchild
                if curr.left.left or curr.left.right:
                    has = True
                stack.append(curr.left)   # still need to check left itself
            if curr.right:
                if curr.right.left or curr.right.right:
                    has = True
                stack.append(curr.right)

            # left or right had a child → this node has a grandchild, keep it
            if has:
                result.append(curr.val)

        return result

    # Height-based (same idea as hasGreatGrandchild lab) — threshold is > 0
    def has_grandchild_height(self, root):
        result = []

        def height(node):
            if node is None:
                return -1

            left_h = height(node.left)
            right_h = height(node.right)

            # Grandchild = 2 levels down → tallest child height must be > 0
            if max(left_h, right_h) > 0:
                result.append(node.val)

            return 1 + max(left_h, right_h)

        height(root)
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
        ({"root": [5, 3, 8, 1, 4]}, [5]),
        ({"root": [10, 5, 15, 3, 7, 13, 18]}, [10]),
        ({"root": [1]}, []),
    ]
    for inputs, expected in test_cases:
        root = TreeNode.from_list(inputs["root"])   # level-order list -> tree
        result = Solution().has_grandchild(root)
        output = result
        passed = _same(output, expected, ordered=False)   # order does not matter for this question
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
