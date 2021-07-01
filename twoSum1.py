# Author: Melissa Perez
# Date: --/--/--
# Description:


def twoNumberSum(array, targetSum):
    # Write your code here.
    # first attempt: two for loops
    # space: O(1), time: O(n^2)
    # using two pointers, keep track per element
    # then iterate over remaining and see if they add up to sum

    array_size = len(array)
    for i in range(array_size):
        for j in range(i + 1, array_size):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []