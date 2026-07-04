class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum

'''
IDEA: go from left, keep current sum, if turns negative, start the sum again; keep max_sum
HOWEVEr, if only negative numbers, max_sum will be negative; then, find maximum neg number and return it; update: i dont think thats true
time complexity: O(n) - only passing each element once
space complexity: O(1)

'''