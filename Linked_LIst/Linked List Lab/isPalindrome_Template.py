from re import S


class Node:
    def __init__(self, data):
        self.data = data
        self.val = data   # alias so Solution.isPalindrome's "val" access works
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")

        if self.head is None:
            return False

        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True

        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


class Solution:
    def isPalindrome(self, head):
        #--------- MODIFY NOTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS ---------#
        # Write your code here

        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        #do a comparision
        front = head
        while prev is not None:
            if prev.data != front.data:
                return False
            prev = prev.next
            front = front.next
        return True
            


        

        #--------- MODIFY NOTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS ---------#


if __name__ == "__main__":
    # Prompts for one line of space-separated numbers, e.g.:
    #
    #   Enter numbers: 1 2 3 2 1
    #
    # Builds the list using LinkedList.insertNode (appending each number in
    # order), then runs isPalindrome on it and prints True/False.
    #
    # Run with:
    #   python3 palindrome_custom_linkedlist.py
    # then type the numbers and press Enter.

    line = input("Enter numbers: ").strip()
    nums = [int(tok) for tok in line.split()] if line else []

    linked_list = LinkedList()
    for i, num in enumerate(nums):
        linked_list.insertNode(num, i)  

    linked_list.printList()

    sol = Solution()
    result = sol.isPalindrome(linked_list.head)

    print(result)
