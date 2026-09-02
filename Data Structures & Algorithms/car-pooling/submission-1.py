class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = {}
        for cnt, l, r in trips:
            passengers[l] = passengers.get(l, 0) + cnt
            passengers[r] = passengers.get(r, 0) - cnt

        trips = [(km, dpass) for km, dpass in passengers.items()]
        trips = sorted(trips, key = lambda x: x[0])
        running = 0
        
        for _, dpass in trips:
            running += dpass
            if running > capacity:
                return False
        return True
