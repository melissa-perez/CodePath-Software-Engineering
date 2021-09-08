def element_frequency(nums, freq):
    freq_map = {}
    nums_length = len(nums)

    for i in range(nums_length):
        if nums[i] not in freq_map:
            freq_map[nums[i]] = 1
        else:
            freq_map[nums[i]] += 1

    for j in range(nums_length):
        if freq_map[nums[j]] == freq:
            return nums[j]
    return None


if __name__ == "__main__":
    print(element_frequency([8, 7, 9, 6, 7, 5, 1], 2))
    print(element_frequency([], 2))
    print(element_frequency([1, 2, 3, 2, 1, 2, 3, 2, 1], 2))