class Solution:
    def countBits(self, n: int) -> List[int]:
        out = [0 for _ in range(n + 1)]
        
        for i in range(n + 1):
            m, r = divmod(i, 2)
            out[i] = out[m] + r
        
        return out

# shifting bits to the left is same as multiplying by 2
# so shifting bits to the right is same as dividing by 2
# so for each number n, find m, r = divmod(n, 2); then, n = 2m + r, and out[n] = out[m] + r
        