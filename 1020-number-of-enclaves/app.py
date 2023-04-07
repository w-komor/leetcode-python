# 1020. Number of Enclaves
# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        m, n = len(grid), len(grid[0])

        for i in range(m):
            dfs(grid, i, 0)
            dfs(grid, i, n - 1)

        for j in range(n):
            dfs(grid, 0, j)
            dfs(grid, m - 1, j)

        # Count the remaining land cells
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count
