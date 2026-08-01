# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0
        q = [(root, float("-inf"))]

        while q:
            node, limit = q.pop()

            if not node: continue
            if node.val >= limit: goods += 1

            q.append((node.left, max(node.val, limit)))
            q.append((node.right, max(node.val, limit)))

        return goods