class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        counts = defaultdict(int)
        counts[0] = 1
        presum = 0
        res = 0
        for num in nums:
            presum += num
            res += counts[presum - k]   # query before inserting
            counts[presum] += 1
        return res