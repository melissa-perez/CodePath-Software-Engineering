# Author: Melissa Perez
# Date: --/--/--
# Description:

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # base case: no character exists
        if not s:
            return -1

        # iterate through whole string, keep count
        char_freq = {}

        for letter in s:
            if letter not in char_freq:
                char_freq[letter] = 1
            else:
                char_freq[letter] += 1

        # go through string again to find index
        string_length = len(s)
        for i in range(string_length):
            if char_freq[s[i]] == 1:
                return i
        return -1