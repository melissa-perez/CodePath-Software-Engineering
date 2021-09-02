
def longest_consecutive_subsequence(nums):
    nums_length = len(nums)
    nums_map = {}

    for i in range(nums_length):
        nums_map[nums[i]] = i

    longest_sub_length = 0

    for j in range(nums_length):
        current_num = nums[j]
        current_longest_length = 1

        if current_num - 1 in nums_map:
            current_longest_length += 1
        while current_num in nums_map:
            if current_num + 1 in nums_map:
                current_longest_length += 1
            current_num += 1
        if current_longest_length > longest_sub_length:
            longest_sub_length = current_longest_length

    return longest_sub_length


if __name__ == "__main__":
    print(longest_consecutive_subsequence([1, 0, 2, 5, 6, 7, 8]))
