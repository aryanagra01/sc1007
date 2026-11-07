class TrieNode:
    def __init__(self):
        self.children = [None] * 26 #array with 26 empty positions
        self.is_end_fof_word = False

root = TrieNode()

for word in ["ccat", "ccap", "bat"]:
    node = root

    for char in word:
        index = ord(char) - ord('a')
        if node.children[index] is None:
            node.children[index] = TrieNode()

        node = node.children[index] #which has a reference the the new trienode object
    
    node.is_end_fof_word = True

