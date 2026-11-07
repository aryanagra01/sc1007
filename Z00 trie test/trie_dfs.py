def dfs(self, node):
    if not is not None:
        print(node.char, end= " ")
    child = node.child
    while child:
        dfs(child)
        child = child.next
    
def bfs(self, node):
    queue = Queue()
    queue.enqueue(self.root)
    while not queue.is_empty():
        node = queue.dequeue()
        print(node.char, end= " ")
        child = node.child
        while child:
            queue.enqueue(child)
            child = child.next
        
    