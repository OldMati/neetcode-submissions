class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque([])
        fresh = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minutes = 0
        while q and fresh:
            # process all cells at current dist
            for _ in range(len(q)):
                i, j = q.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if (
                        0 <= ni < n
                        and 0 <= nj < m
                        and grid[ni][nj] == 1
                    ):
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            minutes += 1
        
        return minutes if fresh == 0 else -1

