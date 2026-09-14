class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, index):
        new_node = Node(data)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            return False

        new_node.next = current.next
        current.next = new_node
        return True

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


class Solution:
    def split(self, head):
        #--------- MODIFY NOTHING ABOVE THIS LINE OR YOUR SOLTUION WILL GET 0 MARKS ---------#
        # Normalize the input: it may arrive as a plain list, a node chain,
        # or a wrapper object with a .head attribute.
        if isinstance(head, list):
            values = head
        else:
            node = getattr(head, 'head', head)
            values = []
            while node:
                values.append(getattr(node, 'data', getattr(node, 'val', None)))
                node = node.next

        even_values = []
        odd_values = []
        for i, value in enumerate(values):
            if i % 2 == 0:
                even_values.append(value)
            else:
                odd_values.append(value)

        return {"even": even_values, "odd": odd_values}
        #--------- MODIFY NOTHING BELOW THIS LINE OR YOUR SOLTUION WILL GET 0 MARKS ---------#

#==============================================================================================
if __name__ == "__main__":
    # Reads one line of space-separated integers, e.g.:
    #
    #   Enter numbers: 1 2 3 4 5
    #
    # Splits into values at even indices (0, 2, 4, ...) and odd indices
    # (1, 3, 5, ...), then prints both lists.
    #
    # Run with:
    #   python3 split_even_odd.py

    line = input("Enter numbers: ").strip()
    nums = [int(tok) for tok in line.split()] if line else []

    # Build the linked list
    linked_list = LinkedList()
    for i, num in enumerate(nums):
        linked_list.insert(num, i)

    # Run the solution directly
    sol = Solution()
    result = sol.split(linked_list)

    print("Even-index values:", result["even"])
    print("Odd-index values:", result["odd"])
