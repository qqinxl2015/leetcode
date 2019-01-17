#https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if not needle:
            return 0
        
        m = len(haystack)
        n = len(needle)
        
        if n > m:
            return -1
        
        if n == m:
            if needle == haystack:
                return 0
            else:
                return -1
        
        k = 0
        for i in range(m-n+1):
            check = True
            #print(i, haystack[i])
            for j in range(n):
                if not haystack[i+j] == needle[j]:
                    check = False
                    break;
            if check:
                return i
        return -1
                
        