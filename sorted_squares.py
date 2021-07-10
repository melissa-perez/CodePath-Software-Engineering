'''
    Input: non-empty array of integers that is sorted.
    Output: new array of squares
'''

def sortedSquaredArray(array):
    # Write your code here.
	# get the size of the array
	arr_size = len(array)
	# have pointers at both ends of the array: start and end
    # need independent index pointer to count down the new sorted list
	start = 0
    end = index = arr_size - 1
	# don't want access errors
	squared_array = [None] * arr_size
	
	while start <= end:
		start_square = array[start] * array[start]
	    end_square = array[end] * array[end]
		
		if start_square > end_square:
			squared_array[index] = start_square
			start += 1
		else:
			squared_array[index] = end_square
		    end -= 1
		index -= 1

    return squared_array