# Author: Melissa Perez
# Date: 08/16/21
# Description:


def firstNonRepeatingCharacter(string):
    """
        Input: String -- lowercase
        Output: Number(int)

        Time: O(N) since you have to iterate through the whole string
        Space: O(1) since the character space is 26(lower case only)
    """
    # assign invalid index
    invalid_index = -1
    # Edge case: empty string
    if not string:
        return invalid_index

    # go through string and keep count of char freq
    char_freq = {}
    for letter in string:
        if letter not in char_freq:
            char_freq[letter] = 1
        else:
            char_freq[letter] += 1

    # iterate through string again to find the first non-repeated
    # char, meaning freq is 1
    string_length = len(string)
    for i in range(string_length):
        if char_freq[string[i]] == 1:
            return i
    # at this point all characters repeated
    return invalid_index
