class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # easiest way is to use the inbuilt compare between of ints and sort

        merged = []
        intervals_length = len(intervals)
        intervals.sort()

        for i in range(0, intervals_length):
            if not merged or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])

        return merged