class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half_sum = total // 2
        res = [[None]*(half_sum + 1) for _ in range(len(nums) + 1)]        # res[i][s]
        def _can_part(i, s):
            if s < 0:
                return False
            if s == 0:
                res[i][s] = True
                return True
            if i == len(nums):
                res[i][s] = False
                return False

            res[i][s] = _can_part(i + 1, s - nums[i]) or _can_part(i + 1, s)
            return res[i][s]
        
        ans = _can_part(0, half_sum)

        return ans

        