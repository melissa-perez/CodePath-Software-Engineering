# Author: Melissa Perez
# Date: --/--/--
# Description:
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m + n length of nums1 w 0s
        # n length of nums2

        total_length = m + n

        nums1_index = m - 1
        nums2_index = n - 1

        for i in range(total_length - 1, -1, -1):
            if nums2_index < 0:
                break
            if nums1_index >= 0 and nums1[nums1_index] >= nums2[nums2_index]:
                nums1[i] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[i] = nums2[nums2_index]
                nums2_index -= 1
