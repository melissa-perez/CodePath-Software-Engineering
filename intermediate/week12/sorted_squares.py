class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
	    # get the size of the array
        arr_size = len(nums)
        # have pointers at both ends of the array: old and new
        start = 0
        end = index = arr_size - 1
        # don't want access errors
        squared_array = [None] * arr_size

        while start <= end:
            start_square = nums[start] * nums[start]
            end_square = nums[end] * nums[end]

            if start_square > end_square:
                squared_array[index] = start_square
                start += 1
            else:
                squared_array[index] = end_square
                end -= 1
            index -= 1

        return squared_array