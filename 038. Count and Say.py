#https://leetcode.com/problems/count-and-say/
class Solution:
    def _countAndSay(n):
        if n == 1:
            return "1"
                
        result_pre = Solution._countAndSay(n-1)
        
        n = len(result_pre)
        
        #print(n, result_pre)
        
        result = ""
        
        tmp = "" 
        count = 0
        for i in range(n):
            ch = result_pre[i]
            
            if tmp == "":
                tmp = ch
                count = 1
            else:
                if tmp == ch:
                    count +=1
                else:
                    result = result + str(count) + tmp
                    tmp = ch
                    count = 1
                    
        if not count == 0:
            result = result + str(count) + tmp
        
        return result
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        return Solution._countAndSay(n)