def singleNumber(self, nums: List[int]) -> int:
	nums_length = len(nums)
	nums_count = {}
	
	for i in range(nums_length):
		if nums[i] not in nums_count:
			nums_count[nums[i]] = 1
		else:
			nums_count[nums[i]]  += 1
	
	for num in nums_count:
		if nums_count[num] == 1:
			return num