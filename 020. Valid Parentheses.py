#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brace = ["(", "{", "["]
        close_brace = [")", "}", "]"]        
        
        braces = {}
        braces[")"] = "("
        braces["}"] = "{"
        braces["]"] = "["
        
        
        order = []
        
        for ch in s:
            if not ch in open_brace and not ch in close_brace:
                continue
            
            if ch in open_brace:
                order.append(ch)
                
            if ch in close_brace:
                if len(order) == 0:
                    return False
                
                last_brace = order[len(order)-1]
                if braces.get(ch) == last_brace:
                    del order[-1]
                else:
                    return False                
        
        
        return len(order) == 0