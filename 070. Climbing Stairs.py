#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        a = [1,2]
        
        tmp = 0
        
        for i in range(n-2):
            tmp = a[0] + a[1]
            a[0] = a[1]
            a[1] = tmp
        
        return tmp