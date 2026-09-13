class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_num = 0
        r = 0
    
        while r < len(nums):
            while r < len(nums)-1 and nums[r] == nums[r+1]:
                r += 1
            nums[next_num] = nums[r]
            next_num += 1
            r += 1

        return next_num

        