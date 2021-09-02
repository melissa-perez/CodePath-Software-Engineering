def runLengthEncoding(string):
    """
	Returns the run-length encoding of a string.
	Input: string
	Output: string
	
	Runtime: O(n) need to iterate the whole string
	Space: O(n) need to possible store n unique characters
	
	"""
	# Base case: null input
	if not string:
		return string
	
	string_length = len(string)
	encoding_list = []
	run_length = 1 

	for i in range(1, string_length): 
		current = string[i] 
		prev = string[i - 1] 
		
		if prev != current or run_length == 9:
			encoding_list.append(str(run_length))
			encoding_list.append(prev)
			run_length = 0

		run_length += 1
	
	encoding_list.append(str(run_length))
	encoding_list.append(string[string_length - 1])

	return "".join(encoding_list)