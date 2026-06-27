class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        # find all rotten fruits, keep them in list
        rotten = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        # do bfs from all rotten fruits; mark each fresh fruit with the (min distance + 2) to a rotten fruit
        for i, j in rotten:
            q = deque([(i, j, 0)])
            
            while q:
                i, j, dist = q.popleft()
                # if empty or already found with lower distance
                if grid[i][j] == 0 or (grid[i][j] >= 2 and grid[i][j] < dist + 2):
                    continue
                
                grid[i][j] = dist + 2
                for di, dj in directions:
                    k, l = i + di, j + dj
                    if k < 0 or k >= n or l < 0 or l >= m:
                        continue
                    q.append((k, l, dist + 1))
        
        # iterate through all cells, if there is still a fresh fruit, return -1, else return max cell number -2
        max_dist = 0
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if val == 1:
                    return -1
                if val > 2:
                    max_dist = max(max_dist, val - 2)
        
        return max_dist 
