"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # sort rooms by start time
        intervals.sort(key=lambda x: x.start)

        # loop over all the intervals
        # keep the queue of end times of currently open rooms
        # for each interval:
        # first pop all rooms that are not needed anymore:
        # while q[0] <= interval.start: q.popleft()
        # then, add the end time of current interval to the queue
        # max_rooms = max(max_roosms, len(q)

        heap = []

        max_rooms = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            max_rooms = max(max_rooms, len(heap))
        
        return max_rooms
