from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        search_queue = []
        if root: search_queue.append(root)
        depth = 0
        while search_queue:
            new_q = []
            while search_queue:
                popped = search_queue.pop()
                if popped.left:
                    new_q.append(popped.left)
                if popped.right:
                    new_q.append(popped.right)
            search_queue += new_q
            depth += 1 
        return depth