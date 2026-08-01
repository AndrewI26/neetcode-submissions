from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0
        q = deque([(root, float("-inf"))])

        while q:
            node, limit = q.pop()
            print(q)

            if not node: continue
            if node.val >= limit: goods += 1

            q.appendleft((node.left, node.val if node.val > limit else limit))
            q.appendleft((node.right, node.val if node.val > limit else limit))

        return goods