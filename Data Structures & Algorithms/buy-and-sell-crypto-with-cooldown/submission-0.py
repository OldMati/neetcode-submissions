class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def _max_prof(i):
            if i >= len(prices):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max([_max_prof(i + 1)] + [prices[j] - prices[i] + _max_prof(j + 2) for j in range(i + 1, len(prices))])
            return memo[i]
        _max_prof(0)
        return memo[0]


'''
subproblem: _max_prof(i):  maximum profit that can be made using only prices[i:]

relation:
at day i, the user can either buy the coin or skip
if he skips, the _max_prof(i) = _max_prof(i + 1)
if he buys, then he must also find a day to sell to maximise profit:
    _max_prof(i) = _max_prof(j + 2) + j - i for j in [i, n]

base case:
_max_prof(i) = 0 for i >= n

org problem
_max_prof(0)

time complexity
n subproblems, so far O(n) work per subproblem (loop j over all [i, n])
thus O(n^2)

topological order
all lower i depend on higher i

'''
        