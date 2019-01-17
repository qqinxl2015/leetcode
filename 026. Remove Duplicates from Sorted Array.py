#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        
        pre = 0
        cur = 0
        n = len(nums)
        
        while cur < n:
            if nums[pre] == nums[cur]:
                cur += 1
            else:
                pre += 1
                nums[pre] = nums[cur]                
                cur += 1
        
        return pre +1
            