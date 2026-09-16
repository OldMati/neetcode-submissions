class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        highest_left = [0] * n      # highest wall to the left from i
        highest_right = [0] * n     # highest wall to the right from i
        highest_left[0] = height[0]
        highest_right[-1] = height[-1]

        # at each position, max water is max(min(highest_left[i], highest_right[i]) - height[i], 0)
        for i in range(1, n):
            highest_left[i] = max(highest_left[i-1], height[i])
            highest_right[-1-i] = max(highest_right[-i], height[-1-i])
        

        res = [max(min(highest_left[i], highest_right[i]) - height[i], 0) for i in range(n)]
        return sum(res)

        