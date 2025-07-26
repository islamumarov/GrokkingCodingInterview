from typing import List
from disjoint_set import DisjointSet

class NumberOfIslands:
    def numIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        disjoint_set = DisjointSet([()])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    disjoint_set.set([i,j])
                    if i > 0 and grid[i-1][j] == '1':
                        disjoint_set.connected((i,j), (i-1, j))
                    if j > 0 and grid[i][j-1] == '1':
                        disjoint_set.connected((i, j), (i, j-1))
                    if i < n-1 and grid[i+1][j] == '1':
                        disjoint_set.connected((i,j),(i+1,j))
                    if j > m-1 and grid[i][j+1] == '1':
                        disjoint_set.connected((i, j), (i, j+1))

        return len(disjoint_set)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = NumberOfIslands()

    print(sol.numIslands(grid))