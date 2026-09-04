class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                sub1 = s[l+1:r+1]   # skip left char
                sub2 = s[l:r]       # skip right char

                return sub1 == sub1[::-1] or sub2 == sub2[::-1]
            l += 1
            r -= 1
        return True