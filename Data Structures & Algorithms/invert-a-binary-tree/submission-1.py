from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        
        search = deque([root])
        while search:
            node = search.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp

            if node.left: search.appendleft(node.left)
            if node.right: search.appendleft(node.right)
        return root