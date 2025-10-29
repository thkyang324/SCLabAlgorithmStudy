# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dia = 0
        def dep(node :Optional[TreeNode]):
            if not node:
                return 0
            right = dep(node.right)
            left = dep(node.left)
            
            if right+left > self.dia:
                self.dia=right+left

            return max(right, left)+1

        dep(root)
        return self.dia