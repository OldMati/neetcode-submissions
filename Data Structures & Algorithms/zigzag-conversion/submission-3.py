class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        num_idx = numRows * 2 - 2
        if num_idx <= 0: num_idx = 1
        for i, char in enumerate(list(s)):
            idx = i % num_idx
            if idx >= numRows:
                idx -= 2 * (idx - numRows + 1)
            rows[idx].append(char)

        return ''.join([''.join(row) for row in rows])
        