#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        res = nums[0]
        cur = nums[0]
        
        for i in range(1,n):
            cur = max(nums[i], nums[i]+ cur)
            res = max(cur, res)
            #print(cur, res)
        
        return res