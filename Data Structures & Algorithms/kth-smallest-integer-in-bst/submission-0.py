# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def flatten(root: Optional[TreeNode]):
    if not root: return []
    return flatten(root.left) + [root] + flatten(root.right)



class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        flat_left = flatten(root.left)
        if len(flat_left) == k - 1:
            return root.val
        if len(flat_left) > k - 1:
            return self.kthSmallest(root.left, k)
        if len(flat_left) < k - 1:
            return self.kthSmallest(root.right, k - 1 - len(flat_left))