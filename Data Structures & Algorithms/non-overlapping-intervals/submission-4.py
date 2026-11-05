class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start time
        intervals = sorted(intervals, key=lambda x: x[1])

        prev_end = float('-inf')
        count = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
        
        return count
