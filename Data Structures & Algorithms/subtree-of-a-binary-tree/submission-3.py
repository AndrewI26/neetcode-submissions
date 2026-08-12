# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isEqual(t1, t2):
    if t1 and t2:
        return t1.val == t2.val and isEqual(t1.left, t2.left) and isEqual(t1.right, t2.right)
    if not t2:
        return True
    
    return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot: return True
        if not root and subRoot: return False
        if not root and not subRoot: return True
        
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:   
            return isEqual(root, subRoot)
        