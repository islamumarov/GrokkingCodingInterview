class ClimbingStairs:
    def climbingStairs(self, n: int) -> int:
        if n == 1:
            return n
        dp = [1, 2]

        for i in range(2, n):
            stairs = dp[i-1] + dp[i-2]
            dp.append(stairs)
        return dp[n-1]




if __name__ == '__main__':
    sol = ClimbingStairs()

    print(sol.climbingStairs(2))