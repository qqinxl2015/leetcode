#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == None or len(s) == 0:
            return 0

        res = 0
        left = -1

        m = {}

        for i, ch in enumerate(s):
            if ch in m:
                v_cur = m.get(ch, -1)
                if v_cur > left:
                    left = v_cur
            m[ch] = i

            res = max(res, i-left)

        return res



        
