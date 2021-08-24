def reverseString(self, s: List[str]) -> None:
	"""
	Do not return anything, modify s in-place instead.
	"""
	# Reverse the input list of chars in place
	# for python we need to use a list
	# the input is a list
	# the output is the same list but reversed

	# edge case: []
	# return []

	# input 1: [a, b, c]
	# output 1: [c, b, a]

	# input 2: [a, b, c, d]
	# output 2: [d, c, b, a]

	# have two pointers
	# start and end
	# swap start and end values
	# until you reach the middle. where the algorithm should end

	list_of_chars_length = len(s)
	start = 0
	end = list_of_chars_length - 1

	while start < end:
		temp = s[start]
		s[start] = s[end]
		s[end] = temp

		start += 1
		end -= 1