#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n_a = len(a) -1
        n_b = len(b) -1
        
        res = ""
        
        carry = 0
        
        while n_a >= 0 or n_b >=0:
            p = a[n_a] if n_a >= 0 else 0
            q = b[n_b] if n_b >= 0 else 0
            
            tmp = int(p) + int(q) + carry
            
            carry = int(tmp/2)
            
            res = str(tmp%2) + res
            
            n_a -= 1
            n_b -= 1
        
        if carry == 1:
            res = "1" + res
            
        return res