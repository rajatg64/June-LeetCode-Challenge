# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invert(self, root):
        if root.left is None and root.right is None:
            return
        root.left, root.right = root.right, root.left
        if root.left:
            self.invert(root.left)
        if root.right:
            self.invert(root.right)
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            self.invert(root)
        return root
        
        