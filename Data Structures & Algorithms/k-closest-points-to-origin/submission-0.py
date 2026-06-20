import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap, if a point is closer than the max in the heap, do a pushpop
        heap = [(float('inf'), [0, 0])] * k #(distance, point(list))

        for point in points:
            x = point[0]
            y = point[1]
            dist_sq = x**2 + y**2
            if dist_sq < heap[0][0]:
                heapq.heappushpop_max(heap, (dist_sq, point))
        
        res = []
        for el in heap:
            res.append(el[1])
        
        return res




        