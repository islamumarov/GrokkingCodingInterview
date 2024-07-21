from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumofLeftLeaves:
    def sumofLeftLeaves(self, root: Optional[TreeNode]):
        if root.left is None and root.right is None:
            return 0
        return self.getLeft(root, False)

    def getLeft(self, root: TreeNode, left):
        if root is None:
            return 0
        if root.left is None and root.right is None and left:
            return root.val
        return self.getLeft(root.left, True) + self.getLeft(root.right, False)



if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    root2 = [1,2,3,4,5]
    root3 = [1]

    solution = SumofLeftLeaves()

    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tree2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    tree3 = TreeNode(1)
    tree4 = TreeNode(0, TreeNode(-4,None,TreeNode(-1, None, TreeNode(3, TreeNode(-2)))),TreeNode(-3, TreeNode(8, None, TreeNode(9, TreeNode(4)))))
    print(solution.sumofLeftLeaves(tree))
    print(solution.sumofLeftLeaves(tree2))
    print(solution.sumofLeftLeaves(tree4))
