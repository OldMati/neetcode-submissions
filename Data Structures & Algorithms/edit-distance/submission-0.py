class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]
            
            # insert/remove/replace character:
            memo[(i, j)] = 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
            return memo[(i, j)]
        
        return dp(0, 0)






'''
SUBPROBLEM: min_dist(i, j) - min distance of word1[i:] to word2[j:]

Orig problem: min_dist(0, 0)

Relation:
at each step: 
- if characters match, increment i and j
- if not:
    - try to insert the word1's character into word2 and vice versa: !!! INSERTING AND DELETING IS THE SAME OPERATION
        - inserting means that the character now matches, so move the opposite pointer to +1 and add one operation
    - try to replace characters with the correct ones; add one operation and move both pointers

Base case:
min_dist(i, j) = 0 if i == len(word1) and j == len(word2)

Time comp:
O(1) per problem (6 cases), n * m subproblems, O(nm)


'''
        