# Author: Melissa Perez
# Date: --/--/--
# Description:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s and t have the same length
        s_length = len(s)
        mappings = {}
        seen = set()

        for i in range(s_length):
            if s[i] not in mappings and t[i] not in seen:
                mappings[s[i]] = t[i]
                seen.add(t[i])
            elif s[i] not in mappings and t[i] in seen:
                return False
            elif mappings[s[i]] != t[i]:
                return False

        return True