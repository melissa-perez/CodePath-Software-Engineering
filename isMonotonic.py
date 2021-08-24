def isMonotonic(array):
	"""
	Input: array of integers
	Output: boolean, true or false

	Case # 1: Input: [], Output: True
	Case # 2: Input: [-1], Output: True
	Case # 3: Input: [-1, -1], Output: True
	Case # 4: Input: [2, 2, -1], Output: False
	Case # 5: Input: [-1, 10], Output: False
	Case # 6: Input: [1, 2, 3], Output: True
	Case # 7: Input: [-1, -100, -1001], Output: True

	We can solve this in-place:
	Run: O(n), need to go through the whole list/array
	Space: O(1), no new data structure

	List problem, iteration
	"""
	
	is_non_decreasing = False
	is_non_increasing = False

	array_length = len(array)
	if array_length <= 1:
		return True
	
	for i in range(1, array_length):
		if not (is_non_decreasing or is_non_increasing):
			if array[i - 1] < array[i]:
				is_non_decreasing = True
			elif array[i - 1] > array[i]:
				is_non_increasing = True
		else:
			if is_non_decreasing:
				if array[i - 1] > array[i]:
					return False
			elif is_non_increasing:
				if array[i - 1] < array[i]:
					return False
	return True