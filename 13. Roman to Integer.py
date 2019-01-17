#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
                
        n = len(s)
        
        res = 0
        
        for i in range(n):
            if i == 0 or symbols.get(s[i], 0) <= symbols.get(s[i-1], 0):
                res += symbols.get(s[i], 0)
            else:
                res += symbols.get(s[i], 0) - 2 * symbols.get(s[i-1], 0)
        
        return res
                