# Q1: First Non-Repeating Character
# Given a string s, return the index of the first character that appears exactly once.
# Use the provided HashTable to count character frequencies.
# hash_insert(key) increments the count, while hash_get(key) returns the count.
# Return -1 if every character repeats or the string is empty.
#
# Example:
# "leetcode"     -> 0
# "loveleetcode" -> 2
# "aabb"         -> -1

    def first_unique_char(self, s):
        ht = HashTable(len(s)) #len is the numdata
        for char in s:
            ht.hash_insert(char) #use defualt vlaue of 1

        for i in range(len(s)):
            if ht.hash_get(s[i]) == 1:
                return i
        return -1
