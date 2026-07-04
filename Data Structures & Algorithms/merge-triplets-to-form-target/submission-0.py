class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        out = [float('-inf')] * 3

        for triplet in triplets:
            replace = False
            skip = False
            for i in range(3):
                if triplet[i] == target[i]:
                    replace = True
                elif triplet[i] > target[i]:
                    skip = True

            if replace and not skip:
                out = [max(triplet[i], out[i]) for i in range(3)]
        
        return target == out

# idea:
# loop over all triplets, loop over the three digits, and if any is the target fill it; if any is greater than target, skip
# if at the end out is target, return true; else return false