
# Q2: Autocomplete (Trie)
#
# Given a list of words and a prefix, return all words
# that start with the prefix in alphabetical order.
#
# Requirements:
# - Create a Trie and insert all the words.
# - Start from the root and follow the prefix characters.
# - If the prefix does not exist in the Trie, return [].
# - From the prefix node, collect all complete words below it.
# - Include the prefix itself if it is a complete word.
# - Sort the collected words alphabetically before returning.
# - If prefix is "", return all words alphabetically.
#
# Examples:
# words = ["car", "card", "care", "cat", "dog"]
#
# prefix = "car" -> ["car", "card", "care"]
# prefix = "ca"  -> ["car", "card", "care", "cat"]
# prefix = "x"   -> []
# prefix = ""    -> ["car", "card", "care", "cat", "dog"]
#
# Task: Complete autocomplete(words, prefix).

    def autocomplete(self, words, prefix):
        trie = Trie()
        for word in words:
            trie.insert(word)

        node = trie.root
        for char in prefix:
            node = trie._find_child(node, char)
            if node is None:
                return []

            #is node is returned its at the end of prefix, so just need all words after
        results = []

        #dfs helper funcion inside 
        def dfs(node, wordSoFar):
            if node.is_end_of_word:
                results.append(wordSoFar)
            child = node.first_child
            while child:
                dfs(child, wordSoFar + child.char)
                child = child.next_sibling
        
        dfs(node, prefix)
        results.sort()
        return results

    def autocomplete(self, words, prefix):
        trie = Trie()
        for word in words:
            trie.insert(word)

        # 1. Walk down to the node for the last character of the prefix.
        node = trie.root
        for char in prefix:
            node = trie._find_child(node, char)
            if node is None:
                return []

        # 2. Collect every word in the subtree below that node.
        results = []

        def collect(current, path):
            if current.is_end_of_word:
                results.append(path)
            child = current.first_child
            while child is not None:
                collect(child, path + child.char)
                child = child.next_sibling

        collect(node, prefix)
        return sorted(results)