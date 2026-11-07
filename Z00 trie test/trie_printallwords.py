def print_all_words_dfs(self, node, prefix):
    if node.is_end_word:
        print(prefix)
    
    child = node.child
    while child:
        self.print_all_words(child, prefix+child.char) #attach a char to a string
        child = child.next

def print_all_words_bfs(self):
    queue = Queue()
    queue.enqueue((self.root, ""))

    while not queue.is_empty():
        node, prefix = queue.dequeue()
        if node.is_end_of_word():
            print(prefix)
        
        child = node.child
        while child:
            queue.enqueue((child, prefix+child.char))
            child = child.next