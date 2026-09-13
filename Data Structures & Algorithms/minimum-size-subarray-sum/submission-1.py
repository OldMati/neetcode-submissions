class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        running = 0 # sum(nums[l:r])
        min_len = float('inf')

        while r < len(nums):
            # if current sum less than target, increment r; else increment l

            if running < target:
                running += nums[r]
                r += 1

            while running >= target:
                min_len = min(min_len, r - l)
                running -= nums[l]
                l += 1
            
        
        return min_len if min_len != float('inf') else 0
        