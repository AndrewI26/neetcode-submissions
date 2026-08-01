# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def flatten(root: Optional[TreeNode]):
            if not root: return []
            return flatten(root.left) + [root.val] + flatten(root.right)
        
        flat = flatten(root)

        for i in range(len(flat)):
            if i == 0: continue
            if flat[i-1] > flat[i]: return False
        return True