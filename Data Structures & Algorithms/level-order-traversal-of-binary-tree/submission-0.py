from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        levels = []

        q = deque([root])
        while q:
            flat_level = []
            len_q = len(q)
            for i in range(len_q):
                node = q.pop()

                flat_level.append(node.val)

                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
                
            levels.append(flat_level)
        return levels