def firstNonRepeatingCharacter(string):
    # Write your code here.
	
	if not string:
		return -1
	
	string_map = {}
	repeated_chars = set()
	
	string_length = len(string)
	
	# going through the string and discovering
	# the non_repeated chars
	for i in range(string_length):
		letter = string[i]
		if letter not in string_map:
			if letter not in repeated_chars:
				string_map[letter] = i
		elif letter in string_map:
			del string_map[letter]
			repeated_chars.add(letter)
	# now we have a dictionary of non_repeated_chars
	index_to_return = string_map[next(iter(string_map))] if string_map else -1
	for key in string_map:
		if string_map[key] < index_to_return:
			index_to_return = string_map[key]
    return index_to_return