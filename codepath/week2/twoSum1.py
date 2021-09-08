# Author: Melissa Perez
# Date: --/--/--
# Description:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_size = len(nums)
        delta_dict = {}

        for i in range(array_size):
            # calculate the missing value
            delta = target - nums[i]
            # if value in dictionary, then we have both summands
            if delta in delta_dict:
                return [delta_dict[delta], i]
            else:
                delta_dict[nums[i]] = i
        # reach the end, no pair found
        return []