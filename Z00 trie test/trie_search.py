def search(self, word):
    node = self.root
    for char in word:
        node = self.find_child(node, char)
        if node is None:
            return False
    return node.is_end_of_word

def find_child_ll (self, node, char):
    current = node.child
    while current:
        if current.char == char:
            return current
        current = current.next
    return None

def find_child_array (self, node, char):
    index = ord(char) - ord('a')
    return node.children[index]

def find_child_dict (self, node, char):
    return node.children.get(char)