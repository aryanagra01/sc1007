class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        current = node.first_child
        while current:
            if current.char == char:
                return current
            current = current.next_sibling
        return None

    def _add_child(self, node, char):
        #add your implementations to insert a child following the alphabetical order
        # linked list insertion

        new_node = TrieNode(char)

        if node.first_child is None or char < node.first_child.char:
            # Insert at the beginning
            new_node.next_sibling = node.first_child
            node.first_child = new_node
            return new_node

        #if nto find correct insertion point
        prev = node.first_child
        current = prev.next_sibling
        while current and current.char < char:
            prev = current
            current = current.next_sibling

        #insert in middle or end
        new_node.next_sibling = current
        prev.next_sibling =  new_node
        return new_node        


    def insert(self, word):
        node = self.root
        for char in word:
            child = self._find_child(node, char)
            if not child:
                child = self._add_child(node, char)
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def dfs(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)

        child = node.first_child
        while child:
            self.dfs(child, prefix + child.char)
            child = child.next_sibling

    def print_words_alphabetically(self):
        #need to create a helper function to make life easy
        self.dfs(self.root, "")

    def dfs_reverse(self, node, prefix):
        #use a satack insead for post order
        stack = Stack()
        child = node.first_child
        while child:
            stack.push(child)
            child = child.next_sibling

        while not stack.is_empty():
            child = stack.pop()
            self.dfs_reverse(child, prefix + child.char)
        
        if node.is_end_of_word:
            print(prefix)

    def print_words_reverse_alphabetically(self):
        self.dfs_reverse(self.root, "")
    
    def dfs_recursion_reverse(self, node, prefix):
        # Visit children in reverse alphabetical order
        self.visit_reverse(node.first_child, prefix)

        # Print current word after exploring children
        if node.is_end_of_word:
            print(prefix)

    def visit_reverse(self, child, prefix):
        if child is None:
            return

        # Visit next sibling first
        self.visit_reverse(child.next_sibling, prefix)

        # Explore the current child's subtree
        self.dfs_reverse(child, prefix + child.char)
        



# Assume Trie, TrieNode, and Queue classes have already been defined.
# Create a new Trie instance
trie = Trie()
trie.insert("car")
trie.insert("care")
trie.insert("cat")
trie.insert("camp")
trie.insert("camera")

trie.print_words_reverse_alphabetically()
trie.print_words_alphabetically()
