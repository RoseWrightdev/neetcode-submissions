class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(row, col, vis, prev):
            if (row, col) in vis:
                return
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return
            if heights[row][col] < prev:
                return
            vis.add((row, col))
            curr = heights[row][col]
            dfs(row + 1, col, vis, curr)
            dfs(row - 1, col, vis, curr)
            dfs(row, col + 1, vis, curr)
            dfs(row, col - 1, vis, curr)

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res





