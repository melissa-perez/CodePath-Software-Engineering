def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    # we are given two sorted arrays of integers
    
    # edge case if one list is empty: return the other one
    # if both are empty return an empty list
    
    # arrays are not the same size, need to make sure comparison stops 
    # before going out of bounds
    
    # input: [], []
    # output: []
    
    #input: [], [1,2,4]
    #output: [1,2,4]
    
    #input: [1,2,4],[3,4,6]
    #output: [1,2,3,4,4,6]
    
    #input: [1,2,3], [9,10]
    #output: [1,2,3,9,10]
    
    if not alices_list:
        return my_list
    if not my_list:
        return alices_list
    
    my_list_length = len(my_list)
    alices_list_length = len(alices_list)
    merge_list_length = my_list_length + alices_list_length
    
    sorted_merged_array = [None] * (merge_list_length)
    merge_index = 0
    my_index = 0
    alices_index = 0
    
    while merge_index < merge_list_length:
        if (alices_index >= alices_list_length or (my_index < my_list_length and my_list[my_index] < alices_list[alices_index])):
            sorted_merged_array[merge_index] = my_list[my_index]
            my_index += 1
        else:
            sorted_merged_array[merge_index] = alices_list[alices_index]
            alices_index += 1
        merge_index += 1
    
    return sorted_merged_array