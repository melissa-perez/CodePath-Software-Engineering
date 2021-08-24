def moveElementToEnd(array, toMove):
	
	left = 0
	right = len(array) - 1
	
	while left <= right:
		if array[right] == toMove:
			right -= 1
			continue
		if array[left] == toMove:
			array[left] = array[right]
			array[right] = toMove
			left += 1
			right -= 1
		else:
			left += 1
	return array