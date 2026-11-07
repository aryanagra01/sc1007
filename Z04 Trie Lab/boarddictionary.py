
# Q3: Board Dictionary (Trie + DFS + Backtracking)
#
# Given a 2D board of letters and a dictionary of words,
# find all dictionary words that can be formed on the board.
#
# Rules:
# - Start from any cell on the board.
# - Move only up, down, left or right (no diagonals).
# - You can change direction while forming a word.
# - Each cell can only be used once per word.
# - Use a Trie to store the dictionary.
# - Return all found words in dictionary order.
# - Do not include words that cannot be formed.
#
# Example:
# board = [
#     ["o", "a", "a", "n"],
#     ["e", "t", "a", "e"],
#     ["i", "h", "k", "r"],
#     ["i", "f", "l", "v"]
# ]
#
# dictionary = ["oath", "pea", "eat", "rain"]
# Output = ["oath", "eat"]
#
# Task: Complete board_dictionary(board, dictionary).

    def board_dictionary(self, board, dictionary):
        # Step 1: Build the Trie
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        result = []
        
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        #Step 2: DFS + Backtracking
        # r, c: coordinates of the cell we want to explore
        # node: current Trie node representing the matched prefix
        # path: word formed so far
        def backtrack(r, c, node, path):

            # Check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Check if cell already visited, becaseu we replaced it with a hashtag
            if board[r][c] == '#':
                return
            
            # Check if letter exists in Trie
            #the node is what is sent in which is following downwards already
            char = board[r][c]
            child = trie._find_child(node, char)

            #if the new node's char is not a child based on the tree, dont do anything and just return
            if child is None:
                return

            # Add letter to current word
            path += char

            # Check if a complete word is found
            if child.is_end_of_word:
                result.append(path)
                #so that we dont kep ading the same word again if multpiple paths can form the word
                child.is_end_of_word = False    
            
            # Mark current cell as visited
            board[r][c] = '#'

            # Explore adjacent cells recursively
            # Pass child as the new Trie node middle since we matched the current letter and moveed one level deeper
            # Pass the updated path containing the letters matched so far
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                backtrack(new_r, new_c, child, path)

            # Backtrack: restore original character
            # After exploring all neighbours, restore the cell
            # so other DFS paths can use it
            board[r][c] = char
        
        #start dfs from every cell
        for row in range(rows):
            for col in range(cols):
                backtrack(row, col, trie.root, "")

        # Step 4: Return words in dictionary order
        #because the results might be in random order
        ordered_result = []
        for word in dictionary:
            if word in result and word not in ordered_result:
                ordered_result.append(word)

        return ordered_result
                

                
