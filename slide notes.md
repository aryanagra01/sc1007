# Slide notes — not in the other four

The other four already have the lab code: linked list, stacks and queues, binary tree and BST, and the infix / prefix / postfix conversions.

This file is the lecture material those notes do not cover. Each section is where it is used, then the content.

## Priority queue — order by urgency, not arrival

A normal queue is FIFO. The one that arrived first leaves first.

A priority queue is an ADT. Each item has data and a priority. The highest priority leaves first, even if it arrived later.

On these slides, a smaller number is a higher priority. Priority 1 is processed before priority 2, before priority 3. Other systems can use a bigger number as higher priority. The rule has to be stated.

| | Normal queue | Priority queue |
| --- | --- | --- |
| Order | FIFO | priority |
| Who leaves first | first arrival | highest priority |
| What decides the order | arrival time | a priority / key |
| Where a new item goes | the rear | wherever its priority belongs |

Example. Arrival order A, B, C, D is not the processing order.

B(P=1) → D(P=2) → C(P=3) → A(P=4). B leaves first.

### Two kinds

| | |
| --- | --- |
| Minimum-priority | smallest key first. Ascending. 7, then 8, then 15, then 20, then 40, then 50. |
| Maximum-priority | largest key first. Descending. 50, then 40, then 20, then 15, then 8, then 7. |

The lecture implementation is a minimum-priority queue. Smaller priority sits nearer the head.

### Where it is used

Computing

- CPU scheduling: the highest-priority waiting job runs next.
- Event simulation: the earliest timestamp is next.
- Dijkstra: the unvisited vertex with the smallest tentative distance.
- Huffman coding: combine the two lowest frequencies, again and again.
- Sorting: insert everything, then keep removing the min or the max.

Real world

- Air-traffic control: emergency, remaining fuel, distance from the runway, waiting time. A later plane can land first.
- Hospital: the more serious patient is seen first.
- Airline standby: membership, fare, check-in time.
- Customer support: a critical request before a routine one.

Use a normal queue when everyone should be treated the same. Use a priority queue when urgency beats arrival time.

### Five ways to build one

The behaviour is the same. The storage changes the cost.

| | Insert | Remove the best |
| --- | --- | --- |
| Unordered array | easy, stick it on the end | search for the best key |
| Ordered array | shift to keep order | the best is already at the front |
| Ordered linked list | walk to the right spot | the best is already at the head |
| Binary heap | both insert and remove stay efficient | |
| BST | another ordered option, if the BST rule is kept | |

The lecture uses the ordered linked list. Highest priority stays at `head`, so peek and dequeue do not search.

### The node

```python
class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
```

### peek — look, do not remove

Empty raises `IndexError`. Otherwise return `head.data`. Head, size, and next do not change.

```python
def peek(self):
    if self.isEmpty():
        raise IndexError("Queue is empty")
    return self.head.data
```

### enqueue — the only operation that searches

Smaller priority goes nearer the front. Equal priority goes behind the ones already there, so equals stay FIFO.

```python
def enqueue(self, data, priority):
    new_node = PriorityNode(data, priority)
    if self.isEmpty() or priority < self.head.priority:
        new_node.next = self.head
        self.head = new_node
    else:
        current = self.head
        while current.next and current.next.priority <= priority:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    self.size += 1
```

Two traces.

Front insert. Queue is 20 with priority 4. New item is 60 with priority 1. `1 < 4`, so the new node points at the old head, then head moves to 60. Order becomes 60(P=1) → 20(P=4). Size goes 1 → 2.

Middle insert. Queue is 40(P=2) → 50(P=4) → 60(P=5). New item is 30 with priority 4. `4 < 2` is false, so walk. Next priority 4 is `<= 4`, so step onto 50. Next priority 5 is not `<= 4`, so stop. Link 30 between 50 and 60.

Order becomes 40(P=2) → 50(P=4) → 30(P=4) → 60(P=5). The new priority 4 sits after the old priority 4. Size goes 3 → 4.

The `<=` is the FIFO part. A strict `<` would put the new equal in front of the old one.

### dequeue — take the head

No search. The best item is already at the front.

```python
def dequeue(self):
    if self.isEmpty():
        raise IndexError("Queue is empty")
    removed_data = self.head.data
    self.head = self.head.next
    self.size -= 1
    return removed_data
```

On 40(P=2) → 50(P=4) → 30(P=4) → 60(P=5), this returns 40 and head becomes 50. Size goes 4 → 3.

### isEmpty and getSize

```python
def isEmpty(self):
    return self.head is None

def getSize(self):
    return self.size
```

`isEmpty` guards peek and dequeue, and tells enqueue that the first node is the head.

`getSize` returns the stored count. Walking from head would also work, and it is the slow version. Every enqueue and dequeue has to update `size`, or the stored count is wrong.

## Array or linked list

| | Array | Linked list |
| --- | --- | --- |
| Memory | one contiguous block | separate nodes |
| Size | fixed, or resized by copying | grows and shrinks |
| Reach an item | index, direct | walk from head |
| Extra memory | low | one reference per node |
| Cache | generally better | generally worse |
| Insert or delete in the middle | shift the later items | change a few links |

Use an array when you jump to an index a lot, and inserts and deletes are rare.

Use a linked list when items keep arriving and leaving, and you do not want to shift everyone after the change. You pay for that by walking from `head`. There is no index jump.

Task scheduling is the lecture example. Each task is a node. A new task is inserted, a finished task is removed, and the scheduler walks to the next one. No block of memory is reserved in advance, so the list can grow and shrink with the load.

### Size

Walking every time is correct and O(n).

```python
def getSize(self):
    count = 0
    current = self.head
    while current is not None:
        count += 1
        current = current.next
    return count
```

The lecture wants a stored `size` instead. Start at 0. Add 1 on insert, subtract 1 on delete. `getSize` just returns `self.size`.

Same idea on the priority queue, the stack, and the queue.

## Which linked list

The insert, delete, and circular stop conditions are already in the linked-list notes. This is only when each shape is the one to use.

| | Use it when | Cost |
| --- | --- | --- |
| Singly | you only walk forward | one `next`. Delete needs the node before the target. |
| Doubly | you also walk backward, or you already hold the node you want to delete | extra `prev` on every node. More links to update. Easier to get a link wrong. |
| Circular singly | the work repeats in a loop, forward only | no `None`. Stop when you are back at the start, or the walk never ends. |
| Circular doubly | that same loop, and you also walk backward | both circular links, and both directions. |

Doubly is used for

- Browser history. Back is `prev`, forward is `next`.
- Undo and redo. Back through old actions, forward to restore them.
- An LRU cache, together with a hash map. The map finds the node. The list moves or removes it without shifting the rest.

Circular is used for

- Round-robin scheduling. Each process gets a turn, then the last one links back to the first.
- A circular buffer for streaming or packets. The lecture says the buffer is the same cycling idea, and it is not always built as a linked list.

## Stack or queue

The lab patterns (reverse, brackets, interleave, delete middle) are already in the stacks-and-queues notes. This is where the lecture says each one belongs.

A stack is LIFO. Only the top is touched. Use it when the newest item has to be handled first.

- Reverse a sequence.
- Nested brackets or HTML tags. The latest opener is the one the next closer must match.
- Function calls and recursion. The latest call finishes before control goes back.
- Expression evaluation. Operands and operators are held until it is their turn. That is the conversion notes.
- Undo in an editor. The last action is the one undone.
- Backtracking and depth-first search. Store the choices still to try, and return to the last one when a path dies.
- Browser back. The page you just left is the first one you return to.

A queue is FIFO. Join at the rear, leave at the front. Use it when arrival order is the processing order.

- Tasks waiting for the CPU, first-come first-served.
- Print jobs, in the order they were sent.
- Network packets, in the order they arrived.
- A stream buffer, so audio or video can be consumed as it arrives.
- GUI events: clicks and keystrokes handled in the order they happened.
- Breadth-first search, and level order on a tree. Nearer nodes are processed before farther ones. The tree notes already have that walk.

A linked queue keeps `front` and `rear` so enqueue and dequeue do not walk the whole list. Built on a `LinkedList`, enqueue is insert at `size` and dequeue is remove index 0. A stack on a `LinkedList` only uses index 0. Same storage, different end.

If the newest should win, it is a stack. If the oldest should win, it is a queue. If some other key should win, it is a priority queue.

## Tree words

A linked list, stack, queue, and priority queue are linear. One item follows one next item.

A tree is not linear. One node can connect to more than one other node.

- Root: the top. No parent. One per tree.
- Edge: the link between a parent and a child.
- Parent: has one or more children.
- Child: directly under its parent.
- Siblings: same parent.
- Ancestor: on the path from this node up to the root.
- Descendant: somewhere below this node.
- Internal node: has at least one child.
- Leaf: no children.

Every node except the root has exactly one parent.

A binary tree is the case where each node has at most two children, `left` and `right`. Either can be `None`. A node stores `data`, `left`, and `right`.

Height on the slides is the number of edges on the longest path from the root to a leaf. A leaf is 0. An empty child is -1. That is the tutorial version already in the tree notes: `1 +` the taller child, empty returns -1.

Traversal is how you visit every node. Depth-first is preorder, inorder, postorder. Breadth-first is level order, and it uses a queue. The walks themselves are in the tree notes.

## BST facts the coding notes assume

Smaller keys go left. Bigger keys go right. Both subtrees are BSTs too.

The lecture implementation does not allow a duplicate. Search and insert compare and take one side. Inorder visits the values in ascending order. The minimum is the leftmost node. The maximum is the rightmost node.

Delete has three cases. The remove code is already in the tree notes.

| | |
| --- | --- |
| No children | a leaf. Set the parent's link to `None`. |
| One child | connect the parent straight to that child. |
| Two children | copy the inorder successor into this node, then delete the successor. |

The successor is the smallest node in the right subtree. Start at `node.right`, then keep going left. The predecessor is the other choice: the largest node in the left subtree.
