class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def build_doubly(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            node.prev = tail
            tail = node
    return head


def values_of(head):
    out = []
    seen = set()
    cur = head
    while cur is not None and id(cur) not in seen:
        seen.add(id(cur))
        out.append(cur.data)
        cur = cur.next
    return out


def make_cycle(values, join_at):
    head = build(values)
    if head is None:
        return None
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    nodes[-1].next = nodes[join_at]
    return head


def bst_insert(root, data):
    if root is None:
        return BTNode(data)
    if data < root.data:
        root.left = bst_insert(root.left, data)
    else:
        root.right = bst_insert(root.right, data)
    return root


def bst_from(values):
    root = None
    for value in values:
        root = bst_insert(root, value)
    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)


class Stack:
    def __init__(self, values=None):
        self._items = []
        if values:
            for value in values:
                self.push(value)

    def push(self, data):
        self._items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def items_top_first(self):
        return list(reversed(self._items))


class Queue:
    def __init__(self, values=None):
        self._items = []
        if values:
            for value in values:
                self.enqueue(value)

    def enqueue(self, data):
        self._items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def items_front_first(self):
        return list(self._items)


def check(name, fn, expected):
    try:
        got = fn()
    except NotImplementedError:
        print(f"skip  {name}")
        return
    except Exception as error:
        print(f"FAIL  {name}  crashed: {error}")
        return
    if got == expected:
        print(f"ok    {name}")
    else:
        print(f"FAIL  {name}")
        print(f"      got      {got}")
        print(f"      expected {expected}")
