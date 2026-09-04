class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        """
        Do not return anything, modify nums in-place instead.
        """
        def _rot_subarr(l, r): # rotate subarray nums[l:r+1]
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # rotate left half, rotate right half, rotate everything
        _rot_subarr(0, n - k - 1)
        _rot_subarr(n - k,n - 1)
        _rot_subarr(0, n - 1)
        