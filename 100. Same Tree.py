#https://leetcode.com/problems/same-tree/
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
        
        return Solution.check(p.left, q.left) and Solution.check(p.right, q.right) 
        
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return Solution.check(p, q)
        
        