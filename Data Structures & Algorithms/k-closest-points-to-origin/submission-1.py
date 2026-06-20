import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap, if a point is closer than the max in the heap, do a pushpop
        heap = [(float('inf'), [0, 0])] * k #(distance, point(list))

        for x, y in points:
            dist_sq = x**2 + y**2
            if dist_sq < heap[0][0]:
                heapq.heappushpop_max(heap, (dist_sq, [x, y]))
        
        res = []
        for el in heap:
            res.append(el[1])
        
        return res




        