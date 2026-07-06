class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def bfs(r, c):
            queue = deque([(r, c)])
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            count = 0
            visit = set([(r, c)])
            while queue:
                n = len(queue)
                for _ in range(n):
                    r, c = queue.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == 0:
                                count += 1
                            elif (nr, nc) not in visit:
                                queue.append((nr, nc))
                                visit.add((nr, nc))
                        else:
                            count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0