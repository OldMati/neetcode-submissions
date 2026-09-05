import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []

        for i, (enq, proc) in enumerate(tasks):
            heap.append((enq, proc, i))
        
        heapq.heapify(heap)

        res = []
        q = []
        time = 1

        while heap or q:    # fulfill all tasks
            while heap and heap[0][0] <= time: # while available tasks, add to queue        
                enq, proc, idx = heapq.heappop(heap)
                heapq.heappush(q, (proc, idx)) # push 

            if q:
                proc, idx = heapq.heappop(q)
                res.append(idx)
                time += proc
            else:
                time = heap[0][0] # skip to next task

        return res
                

        