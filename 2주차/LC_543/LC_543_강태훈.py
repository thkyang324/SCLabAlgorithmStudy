from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        루트 포함하는 경우 => 좌 깊이 + 우 깊이
        루트 포함 안하는 경우 => max(좌 직경, 우 직경)
        """

        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            # print("Node", node.val)
            leftside = dfs(node.left)
            rightside = dfs(node.right)
            self.ans = max(self.ans, leftside + rightside)
            
            return 1 + max(leftside, rightside)

        dfs(root)
        return self.ans
    
if __name__ == "__main__":
    solver = Solution()

    tree_nodes = [TreeNode(i+1, None, None) for i in range(5)]

    tree_nodes[0].left = tree_nodes[1]
    tree_nodes[0].right = tree_nodes[2]

    tree_nodes[1].left = tree_nodes[3]
    tree_nodes[1].right = tree_nodes[4]

    for i in range(5):
        print("Start in {}`th node => Answer: {}".format(i+1, solver.diameterOfBinaryTree(tree_nodes[i])))
