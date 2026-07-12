import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ## DIJKSTRA!!
        # create a hash table of the network 
        # construct a dist array where dist[i] is the current smallest distance from k to i
        
        # loop while heap, pop the node
            # loop over all the children and assign the distances to the children as the min of already found and current;
        # return the key of the node in the heap
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        edges = {}  # edges[u] = {} - dict of all children of u
        # edges[u][v] = int - the time it takes to get from u to v
        for u, v, t in times:   # O(E)
            if u not in edges:
                edges[u] = {}
            
            edges[u][v] = min(edges[u].get(v, float('inf')), t)


        heap = [(0, k)] # O(1)

        while heap:
            distance, u = heapq.heappop(heap)
            if u in edges:
                for v, t in edges[u].items():
                    cur_dist = dist[u] + t

                    if cur_dist < dist[v]:
                        dist[v] = cur_dist
                        heapq.heappush(heap, (cur_dist, v)) 
        
        max_dist = max(dist[1:])
        return -1 if max_dist == float('inf') else max_dist





        