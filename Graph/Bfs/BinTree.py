from queue import Queue
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        q = [TreeNode]
        q.append(root.val)

        while q:
            curr = q.pop(0)
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)

            if curr:
                ans.append(curr.val)



        return ans





if __name__ == '__main__':
    sol = Solution()

    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))

    print(sol.rightSideView(root))
