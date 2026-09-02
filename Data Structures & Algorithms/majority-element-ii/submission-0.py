class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums) // 3
        res = [key for key, val in freq.items() if val > n] 
        return res