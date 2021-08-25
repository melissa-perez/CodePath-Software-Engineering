def rotate(self, nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	nums_length = len(nums)
	rotated_array = [None] * nums_length
	
	for i in range(nums_length):
		rotated_array[(i + k) % nums_length] = nums[i]
	
	for j in range(nums_length):
		nums[j] = rotated_array[j]