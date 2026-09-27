class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

def insert(data, current_node):
   if data < current_node.data:
       if current_node.left is None:
           current_node.left = Node(data)
       else:
           insert(data, current_node.left)
   else:
       if current_node.right is None:
           current_node.right = Node(data)
       else:
           insert(data, current_node.right)

def findMin(node):
   while node.left is not None:
       node = node.left
   return node

def removeBSTNode(node, value):
   if node is None:
        #return the node of the tree and then the status code of whehter it was removed (2 variables)
        #here the number is -1 to say fail and node is still the node (None)
        #also for recursive call until the value doesnt exist in the tree, so then give up
       return node, -1
   
   #basically the search algo first to locate the value
   #if target is on the left
   if value < node.data:
        #calling eveything on the left subtree
       new_left, result = removeBSTNode(node.left, value)

       #in case the node.left was the one deleted, then need to attach the new top
       node.left = new_left
       return node, result

   elif value > node.data:
       new_right, result = removeBSTNode(node.right, value)
       node.right = new_right
       return node, result


   else: #bascially node is found ( == )

        #if there is no left child
       if node.left is None:
            #return right makes it the new head whcih will be attached later bypassing the deleted one
            #and if there was no right, then none is sent back, whcih odesnt matter becasue it meant there was no children anyways
            #nobody to take the spot hence leave it empty to attach
           return node.right, 0
        
        #same for right
       elif node.right is None:
           return node.left, 0

       #this is the case where there are 2 children
       #save the item to delete

       #find the in-order successor
       succ = node.right
       while succ.left is not None:
            succ = succ.left

        #replace the data
       node.data = succ.data

        #delete the old 60 from the right side, _ exsits becasue we do not care about it
        #recursive call so we do not care what happens to it (but it is confirm going to be a case 0 or 1)
        #call from the right itself so the replaced do not get delted
       new_right, _ = removeBSTNode(node.right, succ.data)

       #replae the new right to be attached (could be the same) (only when the immeidate right is the succesrro)
       node.right = new_right
       return node, 0




        #basic idea is find the node first if it even ecists by recurive calling
        #then if found, the node to be remoed is the head
        #check if etiehr one of the children is none
            #then can do case 0/1 where just return opposite child, 0
        #if 2 children
            #find successor
            #replace node data with successor data 
            #then run the remove algo for the successor on the right subtree
            #reattach the right side if neeeded
            #return node, 0
        #when reutrned in the oringal recurive block attach back based on the side the recussion was ran and return the node

def printTree(node, level=0, prefix="Root: "):
   if node is not None:
       print(" " * level + prefix + str(node.data))
       if node.left or node.right:
           if node.left:
               printTree(node.left, level + 4, "L--- ")
           if node.right:
               printTree(node.right, level + 4, "R--- ")

def inorder_traversal(node):
   if node:
       inorder_traversal(node.left)
       print(node.data, end=" ")
       inorder_traversal(node.right)

if __name__ == "__main__":
   root = Node(10)
   
   insert(5, root)
   insert(15, root)
   insert(2, root)
   insert(7, root)
   insert(12, root)
   insert(18, root)
   
   print("Original Tree:")
   printTree(root)
   print("\nIn-Order Traversal of original BST:")
   inorder_traversal(root)
   
   print("\n\nRemoving node with two children (5):")
   root, result = removeBSTNode(root, 5)
   print(f"Remove result: {'Success' if result == 0 else 'Failed'}")
   printTree(root)
   
   print("\nRemoving node with one child (15):")
   root, result = removeBSTNode(root, 15)
   print(f"Remove result: {'Success' if result == 0 else 'Failed'}")
   printTree(root)
   
   print("\nRemoving leaf node (2):")
   root, result = removeBSTNode(root, 2)
   print(f"Remove result: {'Success' if result == 0 else 'Failed'}")
   printTree(root)
   
   print("\nFinal In-order traversal:")
   inorder_traversal(root)