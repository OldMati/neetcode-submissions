class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        n = len(nums)
        while i < n - 1:
            max_jump = nums[i]
            next_pos = i + max_jump
            if next_pos >= n:
                return jumps + 1
            for j in range(1, max_jump + 1):
                max_next_pos = min(n - 1, j + nums[i + j])
                if max_next_pos >= next_pos + nums[next_pos]:
                    next_pos = i + j
            
            jumps += 1
            i = next_pos
        return jumps
                


'''
IDEA: - jump as far as possible including next jump
- start at i = 0
wihle i < n - 1:
    - for each j < nums[i]:
        - compute the total max distance i would jump by jumping to j + nums[i + j], keep max
    - increase jump count
    - jump to the max
    - also, max jump pos is capped at len(nums) - 1     ### IMPORTANT!!!!
'''
        