class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for _ in range(len(s) + 1)]   # can s[0:i] be split into dict words
        memo[0] = True  # empty string can be split

        n = len(s)
        for i in range(n + 1):
            # loop over all j < i, if memo[j] == True, try word = s[j:i] in dict; if true set to true
            for j in range(i):
                if memo[j] and s[j:i] in wordDict:
                    memo[i] = True
                    break



        return memo[-1]
'''
subproblem:
can_be_split(i): can s[i:] be split into dict words; if not, returns residual

relation:
- take residual, add s[i] to beginning, check if in dict:
    - yes: return true and residual = ''
    - no: return False and residual

# instead should:
if can fit the word, should try to move without using it anyway

base case:
i == n:
true, ''

orig problem:
can_be_split(0)


time comp:
n problems, m * t work per problem -> O(nmt)

'''
        