class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # loop over every bit, extract it, push to back
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        
        return res
        