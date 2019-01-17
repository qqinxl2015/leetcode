#https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
        return n