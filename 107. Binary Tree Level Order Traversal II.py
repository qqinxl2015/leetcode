#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        res = []
        
        queue = []
        queue.append(root)
        
        while not len(queue) == 0:
            queueOneLevel = []
            resOneLevel = []
            
            for q in queue:
                if q == None:
                    continue
                
                #print(q.val)
                resOneLevel.append(q.val)
                
                if not q.left == None:
                    queueOneLevel.append(q.left)
                
                if not q.right == None:
                    queueOneLevel.append(q.right)
            
            res.insert(0, resOneLevel)
            queue = queueOneLevel
        
        #print(res)
        
        return res
                
            