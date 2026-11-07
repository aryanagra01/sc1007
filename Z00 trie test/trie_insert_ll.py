def add_child(self, node, char):
    new_node = TrieNode()
    new_node.next = node.child
    node.child = new_node
    return new_node

def find_child_ll (self, node, char):
    current = node.child
    while current:
        if current.char == char:
            return current
        current = current.next
    return None

def insert (self, word):
    node = self.root
    for char in word:
        child = self.find_child(node, char)
        if child is None:
            self.add_child(node, char)
        node = child
    node.is_end_of_word = True