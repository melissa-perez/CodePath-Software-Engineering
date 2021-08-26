def binarySearch(array, target):
	array_length = len(array)
    left = 0
	right = array_length - 1
	
	while left <= right:
		middle = (left + right) // 2

		if array[middle] == target:
			return middle
		elif array[middle] > target:
			right = middle - 1
		elif array[middle] < target:
			left = middle + 1	
	return -1
