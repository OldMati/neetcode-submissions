# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, cur):
            nonlocal res
            cur = cur * 10 + node.val

            if node.left:
                dfs(node.left, cur)
            
            if node.right:
                dfs(node.right, cur)
            
            if not (node.left or node.right):
                res += cur
        
        dfs(root, 0)
        return res
            
        