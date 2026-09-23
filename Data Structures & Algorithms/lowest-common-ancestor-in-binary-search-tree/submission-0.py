# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur_node = root

        left = min(p.val, q.val)
        right = max(p.val, q.val)

        while True:
            if cur_node.val == p.val:
                return p
            elif cur_node.val == q.val:
                return q
            elif left < cur_node.val < right:
                return cur_node
            elif cur_node.val < left:
                cur_node = cur_node.right
            elif cur_node.val > right:
                cur_node = cur_node.left
            