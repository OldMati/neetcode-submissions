class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start, end = newInterval

        res = []
        idx = -1
        for i, (start_i, end_i) in enumerate(intervals):
            if end_i >= start:
                idx = i
                break
            res.append([start_i, end_i])

        if idx == -1:
            return res + [newInterval]

        print(res)
        # now, iterate through the intervals; if interval not overlapping, return
        # interval is overlapping if end > start_i
        first_to_append = idx

        for i, (start_i, end_i) in enumerate(intervals[idx:]):
            if end >= start_i:         
                start = min(start, intervals[idx + i][0])
                end = max(end, intervals[idx + i][1])
            else:
                # not overlapping: add interval and the rest
                return res + [[start, end]] + intervals[idx+i:]
        
        # if were overlapping until the end, return res and last interval
        return res + [[start, end]]



        