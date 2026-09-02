class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        for i in range(1, n):
            word = words[i]
            prefix[i] = prefix[i-1]
            if word[0] in vowels and word[-1] in vowels:
                prefix[i] += 1
                
        res = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            left = prefix[l - 1] if l >= 1 else 0
            res[i] = prefix[r] - left
        return res