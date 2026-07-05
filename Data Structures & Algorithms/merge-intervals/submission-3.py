class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # loop over all intervals; keep the previous start and end
        # if current start is less than previous end, update end and continue
        # else, insert the interval into result

        intervals.sort()
        prev_start, prev_end = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if start > prev_end:
                res.append([prev_start, prev_end])
                prev_start = start

            prev_end = max(prev_end, end)
        
        res.append([prev_start, prev_end])
        return res
                
        