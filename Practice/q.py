"""One question. Fill reverse_list, then run this file.

A list is Node objects. node.data, node.next.
Return the new head.
"""

from _support import build, values_of, check


def reverse_list(head):
    """[1, 2, 3, 4] -> [4, 3, 2, 1]
    [7] -> [7]
    empty -> []
    """
    if head is None:
        return head

    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    
    head = prev
    return head


if __name__ == "__main__":
    check("four nodes", lambda: values_of(reverse_list(build([1, 2, 3, 4]))), [4, 3, 2, 1])
    check("one node", lambda: values_of(reverse_list(build([7]))), [7])
    check("empty", lambda: values_of(reverse_list(None)), [])
