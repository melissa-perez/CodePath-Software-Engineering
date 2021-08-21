def removeDuplicates(self, nums: List[int]) -> int:
    nums_length = len(nums)
    slow = 0
    fast = slow + 1
    
    if not nums:
        return 0
    
    while fast < nums_length:
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]   
        fast += 1
    return slow + 1