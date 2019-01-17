#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or strs == None:
            return ""
        
        m = len(strs)
        
        n = len(strs[0])

        for j in range(n):
            ch = strs[0][j]
            #print(ch)
            for i in range(m):
                if j >= len(strs[i]) or not strs[i][j] == ch:
                    return strs[0][:j]
        return strs[0]
                    