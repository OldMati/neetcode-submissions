class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 1
        while True:
            prefix = strs[0][:i]
            for s in strs:
                if i > len(s) or not s.startswith(prefix):
                    return res

            res = prefix
            i += 1