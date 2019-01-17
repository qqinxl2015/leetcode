#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #prev = nums[0]
        #for number in nums[1:]:
        #    prev = prev ^ number 
        #return prev
        
        return int(2*sum(set(nums)) - sum(nums))