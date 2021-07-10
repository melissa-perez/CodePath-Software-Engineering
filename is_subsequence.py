 """
    Input: Two non-empty array of integers
    Returns: boolean
    
    time-complexity: O(N) worst case will iterate through all of array
    space_complexity: O(1) no data structures created
 
 
 """
 
 
 
 def isValidSubsequence(array, sequence):
    array_length = len(array)
    seq_length = len(sequence)
    array_pointer = seq_pointer = 0
    # while both pointers are less than length of both
    while array_pointer < array_length and seq_pointer < seq_length:
        if array[array_pointer] == sequence[seq_pointer]:
            seq_pointer += 1	
    array_pointer += 1
	# if the length and pointer are the same then the subsequence is valid
    return seq_pointer == seq_length