#https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #return self.getMinDepth(root)
        
        if not root:
            return 0
        
        res = 0
        
        queue = []
        queue.append(root)
        
        while not len(queue) == 0:
            res += 1
            
            queueOneLevel = []
            for q in queue:
                if q.left == None and q.right == None:
                    return res
                if not q.left == None:
                    queueOneLevel.append(q.left)
                if not q.right == None:
                    queueOneLevel.append(q.right)
            
            queue = queueOneLevel
        
        return -1
                
                
        
    
    #def getMinDepth(self, root):
    #    if not root:
    #        return 0
    #    
    #    if not root.left:
    #        return (1 + self.getMinDepth(root.right))
    #    
    #    if not root.right:
    #        return (1 + self.getMinDepth(root.left))
    #    
    #    return (1 + min(self.getMinDepth(root.left), self.getMinDepth(root.right)))