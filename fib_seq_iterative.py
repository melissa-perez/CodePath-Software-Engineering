def getNthFib(n):
    
	"""
	 Assuming n is strictly positive. 
	 Case n == 1: return 0
	 Case n == 2: return 1
	 Case n > 2: return some F(n-2) + F(n-1)
	 We need to keep track of the previous two integers in order to compute F(n)
	 
	 O(n):  time iterative, loop as long as value of n
	 O(1):  space, no extra space required
	"""
	prior_value_1 = 0
	prior_value_2 = 1
    if n == 1:
		return prior_value_1
	elif n == 2:
		return prior_value_2
	for i in range(n, 2, -1):
		sum = prior_value_1 + prior_value_2
		prior_value_1 = prior_value_2
		prior_value_2 = sum
	return sum