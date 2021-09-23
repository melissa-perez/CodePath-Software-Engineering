class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        left = 0
        right = nums_length - 1

        # finding the left out of order
        while left < nums_length - 1:
            if nums[left] > nums[left + 1]:
                break
            left += 1

        if left >= nums_length - 1:
            return 0

        # finding the right out of order
        while right - 1 > 0:
            if nums[right] < nums[right - 1]:
                break
            right -= 1

        # need to find min of array slice, either code or use min
        local_min = min(nums[left:right + 1])

        # need to extend array if there is a larger item on the left
        for i in range(left - 1, -1, -1):
            if nums[i] > local_min:
                left = i

        # need to find max of array slice, either code or use max
        local_max = max(nums[left:right + 1])

        # need to extend array if there is a smaller item on the right
        for i in range(right + 1, nums_length):
            if nums[i] < local_max:
                right = i

        return len(nums[left:right + 1])