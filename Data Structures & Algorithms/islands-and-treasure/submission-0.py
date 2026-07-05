class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water, treasure, land = -1, 0, 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == treasure:
                    queue.append((r, c))
                    visit.add((r, c))
        dist = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in visit:
                        continue
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == water:
                            continue
                        if grid[nr][nc] == land:
                            grid[nr][nc] = dist
                            queue.append((nr, nc))
                            visit.add((r, c))
            dist += 1

            
        