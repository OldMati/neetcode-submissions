class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half_sum = sum(nums) / 2
        if half_sum != int(half_sum):
            return False

        def _can_part(i, s):
            if s == 0:
                return True
            if i == len(nums):
                return False
            
            return _can_part(i + 1, s - nums[i]) or _can_part(i + 1, s)
        

        return _can_part(0, half_sum)

        