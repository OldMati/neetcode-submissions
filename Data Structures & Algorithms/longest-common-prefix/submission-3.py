class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
            i += 1
        
        return strs[0]