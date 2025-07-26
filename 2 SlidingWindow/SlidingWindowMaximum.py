import collections
from typing import List


class SlidingWindowMaximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        out = []
        window_max = -1_000_000_0
        for i, j in range(k, len(nums)):
            local_max = i
            if local_max > window_max:
                queue.append(local_max)

