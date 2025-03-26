# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while True: 
            # Check if current is the correct solution
            if p.val == current.val or q.val == current.val: 
                return current
            if p.val < current.val and q.val > current.val:
                return current 
            if p.val > current.val and q.val < current.val: 
                return current

            # If it isn't the solution, move down the tree
            if p.val < current.val and q.val < current.val: 
                current = current.left 
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else: 
                return current

            