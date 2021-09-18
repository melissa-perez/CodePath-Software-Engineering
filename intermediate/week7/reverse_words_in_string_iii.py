class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        words_length = len(words)

        for i in range(words_length):
            words[i] = words[i][::-1]

        return " ".join(words)