from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return root

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root.left is None and root.right is None:
            return False

        def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not root:
                return False

            if root.val < val:
                return searchBST(root.right, val)
            elif root.val > val:
                return searchBST(root.left, val)
            else:
                return True

        if root is None:
            return False

        if searchBST(root, k - root.val):
            return True
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


if __name__ == '__main__':
    sol = Solution() #[4,2,7,1,3]

    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))

    print(sol.findTarget(root, 9))