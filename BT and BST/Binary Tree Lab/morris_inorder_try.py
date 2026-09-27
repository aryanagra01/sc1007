r"""
Morris inorder. Try this yourself.

Inorder is still left, me, right.
No recursion and no stack. Extra memory stays O(1).

The left subtree's rightmost node (the inorder predecessor) gets a
temporary link to the current node. That link is the "come back later"
that a stack would have stored. After you come back, remove the link,
record the node, and go right.

The tree must look the same when you finish. Every temporary link
has to be cleared.

Sample
        4
       / \
      2   6
     / \ / \
    1  3 5  7

Inorder: 1 2 3 4 5 6 7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, items):
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


def morris_inorder(root):
    # Write your code here #
    return []


def main():
    cases = [
        ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5], [4, 2, 5, 1, 3]),
        ([], []),
        ([8], [8]),
    ]
    for items, expected in cases:
        root = TreeNode.from_list(items)
        got = morris_inorder(root)
        status = "ok" if got == expected else "not yet"
        print(status, "tree", items)
        print("  yours:   ", got)
        print("  expected:", expected)


if __name__ == "__main__":
    main()


# Answer is below. Try the function above first.
def morris_inorder_answer(root):
    result = []
    current = root
    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right is not None and predecessor.right is not current:
                predecessor = predecessor.right
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right
    return result
