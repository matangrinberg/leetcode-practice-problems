import numpy as np


class Solution(object):
    def DFS(self, grid, r, c):
        m, n = grid.shape[0], grid.shape[1]
        grid[r, c] = 0

        if r > 0 and grid[r - 1, c] == 1:
            self.DFS(grid, r - 1, c)

        if r + 1 < m and grid[r + 1, c] == 1:
            self.DFS(grid, r + 1, c)

        if c > 0 and grid[r, c - 1] == 1:
            self.DFS(grid, r, c - 1)

        if c + 1 < n and grid[r, c + 1] == 1:
            self.DFS(grid, r, c + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        m, n = len(grid), len(grid[0])
        grid = np.asarray([[int(float(element)) for element in row] for row in grid])
        islands = 0

        for i in range(0, m):
            for j in range(0, n):
                if grid[i,j] == 1:
                    islands += 1
                    self.DFS(grid, i, j)

        return islands
