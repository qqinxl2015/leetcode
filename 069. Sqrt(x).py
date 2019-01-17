#https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        res = x
        
        while res * res > x:
            res = int((res+ x / res)/2)
            #print(res)
        
        return res