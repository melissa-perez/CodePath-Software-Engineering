def romanToInt(self, s: str) -> int:
	
	roman_dict = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
		"IV": 4,
		"IX": 9,
		"XL": 40,
		"XC": 90,
		"CD": 400,
		"CM": 900
	}
	
	s_length = len(s)
	slow = 0
	fast = slow + 1    
	total = 0
	
	while slow < s_length:
		if fast < s_length and s[slow:fast + 1] in roman_dict:
			total += roman_dict[s[slow:fast + 1]]
			fast += 2
			slow += 2
		else:
			total += roman_dict[s[slow]]
			slow += 1
			fast += 1
					 
	return total
