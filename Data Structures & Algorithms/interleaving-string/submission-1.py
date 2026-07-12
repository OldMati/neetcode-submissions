class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}

        def dp(i, j):
            k = i + j

            if k == len(s3):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < len(s1) and s3[k] == s1[i] and dp(i + 1, j):     # use character from s1; return True if possible to interleave
                return True
            if j < len(s2) and s3[k] == s2[j] and dp(i, j + 1):     # analogous
                return True

            memo[(i, j)] = False
            return False
        
        return dp(0, 0)