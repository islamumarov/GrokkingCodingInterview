from typing import List


class MinimumSizeSubarraySum:
    def minSubarraySum(self, target: int, nums: List[int]) -> int:
        windowStart = 0
        window_sum = 0
        min_len = float('inf')
        for i, j in enumerate(nums):
            window_sum += j
            while window_sum >= target:
                min_len = min(min_len, i - windowStart+1)
                window_sum -= nums[windowStart]
                windowStart += 1
        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    solution = MinimumSizeSubarraySum()
    print(solution.minSubarraySum(7, [2, 3, 1, 2, 4, 3]))
