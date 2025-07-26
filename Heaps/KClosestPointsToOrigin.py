import math
from heapq import heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for i, j in enumerate(points):
            distance = math.sqrt ((0 - j[0])**2 + (0 - j[1])**2)
            heappush(queue, (distance, j))


        ans = []
        for i in range(0,k):
            ans.append(heappop(queue)[1])

        return ans


if __name__ == '__main__':
    sol = Solution()

    print(sol.kClosest([[1,3],[-2,2]],1))