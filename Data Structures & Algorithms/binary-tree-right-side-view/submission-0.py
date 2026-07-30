from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 4 5 ->
# res = [1, 3]
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        search = deque([root])

        while search:
            for i in range(len(search)):
                node = search.popleft()
                print(node.val)
                if i == 0:
                    res.append(node.val)
                if node.right:
                    search.append(node.right)
                if node.left:
                    search.append(node.left)
            
        return res




