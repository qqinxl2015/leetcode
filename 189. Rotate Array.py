#https://leetcode.com/problems/rotate-array/
class Solution:
        
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
             
        n = len(nums)
        k = k%n
        
        if k == 0:
            pass
        
        #print(k)
        
        nums_1 = nums[:n-k]
        nums_2 = nums[n-k:]
        
        #print(nums_1)
        #print(nums_2)
        
        nums[:k] = nums_2
        nums[k:] = nums_1
        