from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float("-inf"), float("+inf"))])

        while q:
            search = q.pop()
            if not search[0]: continue

            if search[0].val > search[1] and search[0].val < search[2]:
                q.appendleft((search[0].left, search[1], search[0].val))
                q.appendleft((search[0].right, search[0].val, search[2]))
            else:
                return False
            
        return True


