class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # loop over all intervals; for each interval, loop forward j for i + 1 <= j < n; if end > intervals[j][0] (j_start), then overlap
        # so remove the one ending later
        # when removing, add j to removed; when iterating, if i in removed, continue
        removed = set()
        n = len(intervals)
        for i, (start, end) in enumerate(intervals):

            if i in removed:
                continue

            for j in range(i + 1, n):

                j_start, j_end = intervals[j]
                # check for overlap
                if j_start < end:
                    if j_end < end:
                        removed.add(i)
                        break
                    else:
                        removed.add(j)
        
        return len(removed)