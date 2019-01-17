#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x ==0:
            return True

        if x < 0:
            return False

        if int(x%10) == 0 and x !=0:
            return False

        ret = 0
        while x > ret:
            ret = ret*10 + int(x%10)
            x = int(x/10)           


        return x == ret or x== int(ret/10)