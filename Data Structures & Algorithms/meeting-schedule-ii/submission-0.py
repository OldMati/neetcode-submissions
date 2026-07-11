"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()

        max_rooms = 0
        count = 0
        # s = 0
        e = 0

        for start in starts:

            if start >= ends[e]: # meeting has ended
                print(f'IF {start=} {e=} {ends[e]=}')
                e += 1           # can move the end 
            else:
                print(f'ELSE {start=} {e=} {ends[e]=}')
                count += 1

            max_rooms = max(max_rooms, count) 

        return max_rooms
        