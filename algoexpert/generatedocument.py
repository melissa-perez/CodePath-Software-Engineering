# Author: Melissa Perez
# Date: --/--/--
# Description:

def generateDocument(characters, document):
    """
    Input: characters(String)
    Input: document(String)

    Output: bool

    O(N + M): size of characters and size of document need to be iterated
    O(C): subset of N characters from characters
    """
    # Edge case no characters given
    if not characters:
        return False
    if not document:
        return True

    char_freq = {}

    # iterate through characters to get freq
    for letter in characters:
        if letter not in char_freq:
            char_freq[letter] = 1
        else:
            char_freq[letter] += 1

    # iterate through document and determine if we have enough chars
    for doc_letter in document:
        if doc_letter in char_freq and char_freq[doc_letter] > 0:
            char_freq[doc_letter] -= 1
        else:
            return False

    # if we make it to the end, the doc can be generated
    return True
