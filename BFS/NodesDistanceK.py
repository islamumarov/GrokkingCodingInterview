from collections import deque
from typing import List

from TreeNode import TreeNode


class NodesDistanceK:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        q = deque()
        parent = {}
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                top = q.popleft()
                if top.left:
                    parent[top.left.val] = top
                    q.append(top.left)
                if top.right:
                    parent[top.right.val] = top
                    q.append(top)

        visited = set()
        q.append(target)

        while k > 0 and q:
            size = len(q)

            for _ in range(size):
                cur = q.popleft()
                visited.add(cur.val)
                if cur.left and cur.left.val not in visited:
                    q.append(cur.left)
                if cur.right and cur.right.val not in visited:
                    q.append(cur.right)

                if cur.val in parent and parent[cur] not in visited:
                    q.append(parent[cur])

            k-1

        ans = []
        while q:
            ans.append(q.popleft().val)

        return ans



if __name__ == '__main__':



