r"""
Zigzag level order. Try this yourself.

This is still BFS. A queue walks row by row.
Even rows stay left to right. Odd rows are reversed.

Return a list of rows, not one flat list.

Sample
        1
       / \
      2   3
     / \   \
    4   5   6

Row 0, left to right:  1
Row 1, right to left:  3 2
Row 2, left to right:  4 5 6

[[1], [3, 2], [4, 5, 6]]
"""

from collections import deque


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


def zigzag_level(root):
    # Write your code here #
    return []


def main():
    cases = [
        ([1, 2, 3, 4, 5, None, 6], [[1], [3, 2], [4, 5, 6]]),
        ([1, 2, 3], [[1], [3, 2]]),
        ([1], [[1]]),
        ([], []),
    ]
    for items, expected in cases:
        root = TreeNode.from_list(items)
        got = zigzag_level(root)
        status = "ok" if got == expected else "not yet"
        print(status, "tree", items)
        print("  yours:   ", got)
        print("  expected:", expected)


if __name__ == "__main__":
    main()


# Answer is below. Try the function above first.
def zigzag_level_answer(root):
    if root is None:
        return []
    queue = deque([root])
    rows = []
    left_to_right = True
    while queue:
        row = []
        for _ in range(len(queue)):
            node = queue.popleft()
            row.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            row.reverse()
        rows.append(row)
        left_to_right = not left_to_right
    return rows
