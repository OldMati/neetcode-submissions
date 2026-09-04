class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(path, i):
            if len(path) == k:
                res.append(path[:])
                return
            if i > n:
                return
            
            # either take this number or skip it
            path.append(i)
            backtrack(path, i+1)
            path.pop()

            backtrack(path, i+1)
        
        backtrack([], 1)
        return res


        