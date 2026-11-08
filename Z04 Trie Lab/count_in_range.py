# Question: Lexicographical Range Query
#
# Given a Trie containing lowercase English words and two strings L and R,
# count how many words are lexicographically between L and R (inclusive).
#
# Return the number of words within the range.
#
# Example:
# Words: ["cat", "car", "care", "camera", "dog"]
# L = "car", R = "cart"
# Output: 2
#
# Restrictions: Cannot use list.sort(), set(), or dict().


def count_in_range(trie, L, R):
    node = trie.root

    if L > R:
        L, R = R, L
    
    def dfs(node, prefix):

        count = 0

        if node is None:
            return 0
        
        if node.is_end_of_word:
            if L <= prefix <= R:
                count += 1            
                

        child = node.first_child
        while child:
            count += dfs(child, prefix + child.char)
            child = child.next_sibling
        
        return count

    return dfs(node, "")

