class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = end = 0
        last_idx = {c: i for i, c in enumerate(s)}

        res = []

        for i, c in enumerate(s):
            end = max(end, last_idx[c])

            if i == end:
                res.append(end + 1 - start)
                start = end + 1
            
        
        return res