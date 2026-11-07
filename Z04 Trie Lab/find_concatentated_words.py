# Q4: Concatenated Words (Trie)
# Given a dictionary of words, find all words that can be formed
# by joining 2 or more shorter words from the same dictionary.
# You may use a Trie to store and search the words.
#
# Example:
# Input: ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
#         "hippopotamuses", "rat", "ratcatdogcat"]
# Output: ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
#
# Return all concatenated words in any order.

def find_concatenated_words(dictionary):
    trie = Trie()

    # Step 1: Insert all words into Trie
    for word in dictionary:
        if word:
            trie.insert(word)
            
    #word	The original word we're checking
    #start	The index where we begin checking the remaining characters
    #count	How many complete dictionary words we've already found
    def can_word(word, start, count)

        #check if we reach end of orignial word
        if start == len(word)
            #so that if like cat and the word is ca, it doesnt get sent back
            #This prevents a normal dictionary word from being incorrectly classified as concatenated.
            return count >= 2
        
        #we want to check the new word from the node again becaseu the tire sats from the roots
        node = trie.root

        #
        for i in range(start, len(word)):
            node = trie._find_child(node, word[i])

            if not node:
                return False

