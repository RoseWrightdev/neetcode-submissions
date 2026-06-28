class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                for _ in range(len(queue)):
                    pos = queue.popleft()
                    r, c = pos[0], pos[1]
                    if grid[r][c] == '1':
                        grid[r][c] = '0'
                    else:
                        continue
                    for dx, dy in dirs:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < rows and 0 <= nc < cols:
                            queue.append((nr, nc))
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
        return islands