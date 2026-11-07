
# Q1: Longest Common Prefix (Trie)
#
# Given a list of words, find the longest prefix shared by ALL words.
#
# Requirements:
# - Insert all words into the Trie first.
# - Start from the root and follow the common path.
# - Stop if the current node has more than one child (branching).
# - Stop if the current node marks the end of a word.
# - Trie uses first_child and next_sibling (linked list).
# - Return the longest common prefix as a string.
# - Return "" if no common prefix or the list is empty.
#Because every word must share the same prefix, there can only be one path to follow in the Trie.
#
# Examples:
# ["flower", "flow", "flight"] -> "fl"
# ["dog", "racecar", "car"] -> ""
# ["inter", "interview", "internet"] -> "inter"
# ["", "apple"] -> ""
#
# Task: Complete longest_common_prefix(words).

    def longest_common_prefix(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        node = trie.root
        prefix = ""

        # Continue while there is exactly one child
        # and the current node is not the end of a word, Because the longest common prefix cannot be longer than the shortest word!
        while (node.first_child is not None and node.first_child.next_sibling is None and not node.is_end_of_word):
            
            # Move to the only child
            node = node.first_child

            # Add its character to the prefix
            prefix += node.char

        return prefix


