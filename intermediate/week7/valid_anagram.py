# Author: Melissa Perez
# Date: --/--/--
# Description:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = {}
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        for i in range(s_length):
            if s[i] not in s_count:
                s_count[s[i]] = 1
            else:
                s_count[s[i]] += 1

        for letter in t:
            if letter in s_count and s_count[letter] > 0:
                s_count[letter] -= 1
            else:
                return False

        return True