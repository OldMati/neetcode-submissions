class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # backtrack
        chars = [
            [], [],             # 0, 1
            ['a', 'b', 'c'],    # 2
            ['d', 'e', 'f'],    # 3
            ['g', 'h', 'i'],    # 4
            ['j', 'k', 'l'],    # 5
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],   # 7
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']    # 9
        ]

        res = []

        def backtrack(path, i):
            if i == len(digits):
                res.append(''.join(path))
                return

            for char in chars[int(digits[i])]:
                path.append(char)
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        return res
        