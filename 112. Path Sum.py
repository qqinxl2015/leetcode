#https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        if not root:
            return False
        
        queue = {}
        queue[root] = root.val
        
        while not len(queue) == 0:
            
            queueOneLevel = {}
            for q, v in queue.items():
                if q.left == None and q.right == None:
                    if v == sum:
                        return True
                    
                if not q.left == None:
                    queueOneLevel[q.left] = v + q.left.val
                    
                if not q.right == None:
                    queueOneLevel[q.right] = v + q.right.val
            
            queue = queueOneLevel
        
        return False