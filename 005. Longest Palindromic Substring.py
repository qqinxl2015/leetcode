#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def search(self, s, left, right, start, maxLen):
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        if maxLen < right - left -1:
            start = left +1
            maxLen = right - left -1

        return start, maxLen

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)

        if n < 2:
            return s

        maxLen = 0
        start = 0

        for i, ch in enumerate(s):
            start, maxLen = self.search(s, i, i, start, maxLen)
            start, maxLen = self.search(s, i, i+1, start, maxLen)

        return s[start:start + maxLen]
