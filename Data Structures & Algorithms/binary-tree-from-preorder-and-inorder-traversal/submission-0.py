# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        val_to_idx = {val: idx for idx, val in enumerate(inorder)}
        pre_i = 0

        def build(lo, hi):
            nonlocal pre_i
            if lo > hi:
                return None
            
            # construct root of subtree from leftmost unused preorder node
            val = preorder[pre_i]
            pre_i += 1
            node = TreeNode(val)
            mid = val_to_idx[val]
            node.left = build(lo, mid-1)
            node.right = build(mid+1, hi)
            return node
        
        return build(0, len(preorder)-1)

        