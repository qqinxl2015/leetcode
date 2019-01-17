#https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        
        p = 1
        
        for i in range(n):
            d = digits[n-i-1]
            #print(d)
            
            if p == 0:
                return digits
            else:
                digits[n-i-1] = (d + p) % 10
                p = int((d + p)/10)
                
        if p == 1:
            digits.insert(0, 1)
            
        return digits;
                
            
            