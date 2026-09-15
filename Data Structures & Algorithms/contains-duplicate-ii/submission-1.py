class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {} # map num to last seen index

        for i, num in enumerate(nums):
            if num in last_idx:
                j = last_idx[num]
                if i - j <= k:
                    return True
            last_idx[num] = i
        return False
            
        