#https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(n):
            if not nums[i] == val:
                nums[res] = nums[i]                
                res += 1
        return res