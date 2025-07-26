from itertools import product
from typing import List

from sqlalchemy import false


class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0



if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    sol = NumberOfIslands()
    print(sol.numIslands(grid))