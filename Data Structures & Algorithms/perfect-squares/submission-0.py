class Solution:
    def numSquares(self, n: int) -> int:
        # construct array to iterate on
        arr = []
        total = 0
        i = 1
        while i**2 <= n:
            arr.append(i**2)
            i += 1
        
        arr = arr[::-1]
        # Subproblem: _num_squares(i, t) - min number of squares from arr needed to sum up to t using only arr[i:]
        # relation: _ns(i, t) = min of using this and skipping

        memo = [{} for _ in range(len(arr))]
        arr_len = len(arr)
        def _num_squares(i, t):
            if t == 0:
                return 0
            elif i == arr_len or t < 0:
                return float('inf')
            
            if t in memo[i]:
                return memo[i][t]
            
            memo[i][t] = min(
                1 + _num_squares(i, t-arr[i]),
                _num_squares(i+1, t)
                )
            return memo[i][t]

        ans = _num_squares(0, n)
        return ans
