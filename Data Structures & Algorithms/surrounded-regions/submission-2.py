class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find all 'O' cells on te border in O(n + m) time
        border_cells = []
        for i in range(len(board)):
            for j in (0, len(board[0]) - 1):
                if board[i][j] == 'O':
                    border_cells.append((i, j))
        
        for i in range(len(board[0])):
            for j in (0, len(board) - 1):
                if board[j][i] == 'O':
                    border_cells.append((j, i))
        
        q = deque(border_cells)
        visited = set()
        not_surrounded = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(board)
        n = len(board[0])
        # do bfs from all cells at the same time; keep visited in a set
        # during bfs, go all directions; if 'x' or visited, continue; else, add to not_surrounded and keep searching
        while q:
            i, j = q.popleft()
            visited.add((i, j))
            not_surrounded.add((i, j))
                
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                # make sure ni, nj within board and not visited and not 'x'
                if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in visited or board[ni][nj] == 'X':
                    continue
                q.append((ni, nj))
        
        print(not_surrounded)
        # now, all iterate over whole grid, and if not in not_surrounded, then change it to X
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == 'O' and (i, j) not in not_surrounded:
                    board[i][j] = 'X'
                
                

        