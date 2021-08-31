def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
	
	nums1_length = len(nums1)
	nums2_length = len(nums2)
	
	nums1_dict = {}
	intersect = set()
	
	for i in range(nums1_length):
		if nums1[i] not in nums1_dict:
			nums1_dict[nums1[i]] = i
	
	for j in range(nums2_length):
		if nums2[j] in nums1_dict and nums2[j] not in intersect:
			intersect.add(nums2[j])
			
	return list(intersect)
