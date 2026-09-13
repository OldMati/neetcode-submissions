class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = []
        p1 = 0
        p2 = 0
        n1 = len(word1)
        n2 = len(word2)

        while p1 < n1 or p2 < n2:
            ch1 = word1[p1] if p1 < n1 else ''
            ch2 = word2[p2] if p2 < n2 else ''
            res.append(ch1)
            res.append(ch2)
            p1 += 1
            p2 += 1

        return ''.join(res)
        