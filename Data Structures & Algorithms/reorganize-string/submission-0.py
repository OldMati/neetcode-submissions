import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        # make max heap of frequencies
        heap = [(f, char) for char, f in Counter(s).items()]
        
        heapq.heapify_max(heap)

        if heap[0][0] >= n / 2 + 1:
            return ''
        
        res = []
        while len(heap) > 1: # pop two chars with max frequency at a time, append them to res, push back onto heap
            f1, ch1 = heapq.heappop_max(heap)
            f2, ch2 = heapq.heappop_max(heap)
            res.append(ch1)
            res.append(ch2)

            if f1 - 1 > 0:
                heapq.heappush_max(heap, (f1 - 1, ch1))
            if f2 - 1 > 0:
                heapq.heappush_max(heap, (f2 - 1, ch2))
        
        last = heap[0][1] if heap else ''
        return ''.join(res + [last])

        