#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def change(self, nums, left, right):
        if left > right:
            return None
        
        mid = left + int((right -left)/2)
        #print("left={0} right={1} mid={2} nums[mid]={3}".format(left, right, mid, nums[mid]))
        cur = TreeNode(nums[mid])
        cur.left = self.change(nums, left, mid -1)
        cur.right = self.change(nums, mid +1 , right)
        
        return cur
        
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.change(nums, 0, len(nums)-1)