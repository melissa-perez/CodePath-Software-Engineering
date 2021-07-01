def twoNumberSum(array, targetSum):
    # Write your code here.
    # used array_element as key, since unique
	# space consideration: O(N): might iterate whole array
	# time consideration: O(N): might iterate whole array
    array_size = len(array)
    delta_dict = {}
	
    for i in range(array_size):
	# calculate the missing value
	delta = targetSum - array[i]
	# if value in dictionary, then we have both summands
	if delta in delta_dict:
		return [delta, array[i]]
	else:
	   delta_dict[array[i]] = delta
	# reach the end, no pair found
	return []

