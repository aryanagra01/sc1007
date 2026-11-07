class TrieNode: 
    def __init__ (self):
        self.children = {}
        self.is_end_fof_word = False

root = TrieNode()

for word in ["ccat" , "ccap", "bat"]:

    node = root #node is the travller we follow
    
    for char in word:
        if char not in node.children: #which starts at the root and moves down slowly
            node.children[char] = TrieNode() #create a new trienode for the child, with the key being the charactr

        #if not if it exsits, or once you create the child, move down to the next
        node = node.children[char] #node will now point to the child trienode
    
    #once all chars finish, set the boolean to true for the last trie_node
    node.is_end_fof_word = True