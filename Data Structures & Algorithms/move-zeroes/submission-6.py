class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_num = 0
        n = len(nums)

        for i in range(n):
            while nums[next_num] != 0:
                next_num += 1
                if next_num >= n:
                    return
            
            if i > next_num and nums[i] != 0:
                nums[i], nums[next_num] = nums[next_num], nums[i]
        
             

        