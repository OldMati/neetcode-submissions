class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        n = len(nums)
        while i < n - 1:
            max_jump = nums[i]
            next_pos = i + max_jump
            if next_pos >= n - 1:
                return jumps + 1
            for j in range(1, max_jump + 1):
                max_next_pos = min(n - 1, i + j + nums[i + j])
                if max_next_pos >= next_pos + nums[next_pos]:
                    next_pos = i + j
            jumps += 1
            i = next_pos
        return jumps
                