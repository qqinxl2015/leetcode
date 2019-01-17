#https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(p,q):        
        if p == None and q == None:
            return True
        
        if p == None and not q == None:
            return False
        
        if not p == None and q == None:
            return False
        
        if not p.val == q.val:
            return False
        
        return Solution.check(p.left, q.right) and Solution.check(p.right, q.left) 
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return Solution.check(root.left, root.right)