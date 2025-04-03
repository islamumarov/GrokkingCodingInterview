from typing import List


class IslandPerimeter:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        max_square = -1
        n = len(land)
        m = len(land[0])
        dp = [[n] * 0 for i in range(m)]

        for i in range(n):
            for j in range(m):
                if land[i][j] == 0: continue

            left, top, diag = (dp[i - 1][j] if i > 0 else 0), (dp[i][j - 1] if j > 0 else 0), (
                dp[i - 1][j - 1] if i > 0 and j > 0 else 0)

            dp[i][j] = min([left, top, diag]) + 1
            if max_square < dp[i][j]:
                max_square = dp[i][j]

        return max_square


if __name__ == '__main__':
    array = [[0, 1, 1, 0, 1],
             [1, 1, 0, 1, 0],
             [0, 1, 1, 1, 0],
             [1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0]]

    print(findIsland(array))