# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root is not None:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


