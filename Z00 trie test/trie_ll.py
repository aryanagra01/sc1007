class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.child = None
        self.next = None
        self.is_end_of_word = False

root = TrieNode()

for word in ["ccat", "ccap", "bat"]:
    node = root

    for char in word:
        current = node.child
        previous = None

        while current is not None and current.char != char:
            previous = current
            current = current.next
        
        if current is None:
            current = TrieNode(char)

            if previous is None:
                node.child = current
            else:
                previous.next = current

        node = current

    node.is_end_of_word = True