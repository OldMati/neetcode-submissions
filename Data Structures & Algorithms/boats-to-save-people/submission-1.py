class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the people; then go two pointers from right and left
        # if sum <= limit, increase count and move both pointers; else only move right
        people.sort()
        l = 0
        r = len(people) - 1
        
        count = 0
        while l <= r:
            print(l, r)
            count += 1  
            if people[l] + people[r] <= limit:  # only put left if possible
                l += 1

            r -= 1 # always put the right person on the boat
        return count
            
