#https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return (not self.checkDepth(root) == -1)
        

    def checkDepth(self, root):
        if not root:
            return 0
        
        left = self.checkDepth(root.left)
        
        if left == -1:
            return -1
        
        right = self.checkDepth(root.right)
        
        if right == -1:
            return -1
        
        diff = abs(left - right)
        
        if diff > 1:
            return -1
        
        print(left, right)
        return (1 + max(left, right))
        
        
        
    
    #def isBalanced(self, root):
    #    """
    #    :type root: TreeNode
    #    :rtype: bool
    #    """
    #    if not root:
    #        return True
    #    
    #    diff = abs(self.getDepth(root.left) - self.getDepth(root.right))
    #    
    #    if diff > 1:
    #        return False
    #    
    #    return self.isBalanced(root.left) and self.isBalanced(root.right)
    #        
    #
    #def getDepth(self, root):
    #    if not root:
    #        return 0
    #    
    #    return (1 + max(self.getDepth(root.left), self.getDepth(root.right)))
    
    
    
    