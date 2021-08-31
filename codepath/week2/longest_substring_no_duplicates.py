def lengthOfLongestSubstring(self, s: str) -> int:
	
	start_index = 0
	s_length = len(s)
	
	last_seen = {}
	longest_substring = ""
	
	for i in range(s_length):
		if s[i] not in last_seen: 
			last_seen[s[i]] = i
		else:
			start_index = max(start_index, last_seen[s[i]] + 1)
			last_seen[s[i]] = i
			
		current_substring = s[start_index:i + 1]
		# not optimal
		if len(longest_substring) < len(current_substring):
			longest_substring = current_substring
			
	
	return len(longest_substring)
	