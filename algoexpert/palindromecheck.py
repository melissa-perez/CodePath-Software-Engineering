# Author: Melissa Perez
# Date: --/--/--
# Description:


def isPalindrome(string):
    # Write your code here.
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
