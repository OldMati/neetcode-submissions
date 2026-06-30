class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_here = nums[0]
        min_here = nums[0]

        for num in nums[1:]:
            max_prev = max_here
            min_prev = min_here

            max_here = max(num, num * max_prev, num * min_prev)
            min_here = min(num, num * max_prev, num * min_prev)
            result = max(max_here, result)
        
        return result