class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            return s == s[::-1]
        
        # idea: use backtracking
        # if i == len(s), return
        # check if path is palindrome; if yes, add to result
        # two choices: use characted, or just return (only substrings)
        res = []
        def backtrack(path, i):
            print(f'{i=} {path=}')
            if i >= len(s):
                res.append(path[:])
                return
            # loop over j > i 
            # if s[i:j + 1] is a palindrome, add to path and backtrack
            for j in range(i, len(s)):
                if is_palindrome(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    backtrack(path, j + 1)
                    path.pop()

        backtrack([], 0)
        
        return res

        