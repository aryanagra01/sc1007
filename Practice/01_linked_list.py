"""
Linked list practice. Fill each function, then run this file.

A list is Node objects. node.data, node.next, and node.prev for doubly.
Return the head, because deleting or moving the first node changes it.
"""

from _support import Node, build, build_doubly, values_of, make_cycle, check


def remove_at(head, index):
    """Delete the node at index. 0 is the head.
    [10, 20, 30, 40], index 2 -> [10, 20, 40]
    [10, 20, 30, 40], index 0 -> [20, 30, 40]
    """
    




def remove_duplicates_sorted(head):
    """Sorted list. Delete the extra copies. Keep one of each value.
    [1, 1, 2, 2, 2, 3] -> [1, 2, 3]
    """

    cur = head 
    while cur:
        if cur.next = cur.next.next:
            cur.next = cur.next.next
        else:
            cur = cur.next

def move_max_to_front(head):
    """Move the first maximum node to the front. Leave the rest in order.
    [4, 2, 9, 1] -> [9, 4, 2, 1]
    Already at the front: leave the list alone.
    """
    raise NotImplementedError


def move_min_to_front(head):
    """Move the minimum node to the front.
    [4, 2, 9, 1] -> [1, 4, 2, 9]
    """
    raise NotImplementedError


def move_even_to_back(head):
    """Even values move to the back. Odds stay in front. Keep each group's order.
    [1, 2, 3, 4, 6, 5] -> [1, 3, 5, 2, 4, 6]
    """
    raise NotImplementedError


def move_odd_to_back(head):
    """Odd values move to the back. Evens stay in front. Keep each group's order.
    [1, 2, 3, 4] -> [2, 4, 1, 3]
    """
    raise NotImplementedError


def reverse_doubly(head):
    """Reverse a doubly linked list. Fix both next and prev.
    [1, 2, 3, 4] -> [4, 3, 2, 1]
    """
    raise NotImplementedError


def is_palindrome(head):
    """True if the values read the same forwards and backwards.
    [1, 2, 2, 1] -> True
    [1, 2, 3] -> False
    """
    raise NotImplementedError


def cycle_length(head):
    """Length of the cycle. 0 if there is no cycle.
    1 -> 2 -> 3 -> 4 -> 2  has length 3
    """
    raise NotImplementedError


def find_union(head1, head2):
    """Both lists are sorted. Return a new sorted list of the unique values.
    Do not change the two input lists.
    [1, 2, 2, 3] and [2, 3, 4] -> [1, 2, 3, 4]
    """

    dummy = Node(0)
    tail = dummy
    
    l1 = head1
    l2 = head2

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            tail = tail.next
        else:
            



def split_even_odd_index(head):
    """Split by index, not by value.
    Index 0, 2, 4, ... go in even. Index 1, 3, 5, ... go in odd.
    [1, 2, 3, 4, 5] -> ([1, 3, 5], [2, 4])
    """
    even = []
    odd = []
    cur = head
    i = 0
    while cur is not None:
        if i % 2 == 0:
            even.append(cur.data)
        else:
            odd.append(cur.data)
        cur = cur.next
        i += 1
    return even, odd


if __name__ == "__main__":
    check("remove middle", lambda: values_of(remove_at(build([10, 20, 30, 40]), 2)), [10, 20, 40])
    check("remove head", lambda: values_of(remove_at(build([10, 20, 30, 40]), 0)), [20, 30, 40])
    check("remove duplicates", lambda: values_of(remove_duplicates_sorted(build([1, 1, 2, 2, 2, 3]))), [1, 2, 3])
    check("move max", lambda: values_of(move_max_to_front(build([4, 2, 9, 1]))), [9, 4, 2, 1])
    check("max already front", lambda: values_of(move_max_to_front(build([9, 4, 2]))), [9, 4, 2])
    check("move min", lambda: values_of(move_min_to_front(build([4, 2, 9, 1]))), [1, 4, 2, 9])
    check("even to back", lambda: values_of(move_even_to_back(build([1, 2, 3, 4, 6, 5]))), [1, 3, 5, 2, 4, 6])
    check("odd to back", lambda: values_of(move_odd_to_back(build([1, 2, 3, 4]))), [2, 4, 1, 3])
    check("reverse doubly", lambda: values_of(reverse_doubly(build_doubly([1, 2, 3, 4]))), [4, 3, 2, 1])
    check("palindrome yes", lambda: is_palindrome(build([1, 2, 2, 1])), True)
    check("palindrome no", lambda: is_palindrome(build([1, 2, 3])), False)
    check("cycle", lambda: cycle_length(make_cycle([1, 2, 3, 4], 1)), 3)
    check("no cycle", lambda: cycle_length(build([1, 2, 3, 4])), 0)
    check("union", lambda: values_of(find_union(build([1, 2, 2, 3]), build([2, 3, 4]))), [1, 2, 3, 4])
    check("split index", lambda: split_even_odd_index(build([1, 2, 3, 4, 5])), ([1, 3, 5], [2, 4]))
