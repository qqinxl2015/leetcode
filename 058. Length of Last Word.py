#https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        n = len(s)
        
        if n == 0:
            return 0
        
        res = 0
        
        for i in range(0,n):
            #print(s[i], res)
            if not s[i] == ' ':
                if not i ==0 and s[i-1] == ' ':
                    res = 1
                else:
                    res += 1
        
        return res